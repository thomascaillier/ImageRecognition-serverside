import base64
import io

from django.core.files import File
from numpy import random

from app.models import Image, CorrespondingImages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from processor.Processor import Processor


# This method is called for initiate the process sending the image to proceed
@csrf_exempt
@require_POST
def post_image(request):

    # Retrieve image data sent
    request_image = request.POST.get('image') or request.FILES.get('image')
    if request_image is not None:
        request_image = request_image.file
    else:
        return JsonResponse({"Success": False, "Message": "Post data error: no 'image' field"})

    # Create empty Image object in DB
    image = Image()
    image.save()
    if image.id is None:
        image.delete()
        return JsonResponse({"Success": False})

    # Save image and store path in DB
    image.base_image.save('IMG_'+str(image.id)+'.jpg', File(request_image))

    # Return response
    if image.base_image is not None:
        return JsonResponse({"Success": True, "Key": image.id}, status=201)
    else:
        image.delete()
        return JsonResponse({"Success": False})

ID_KEY = 'Id_'
IMAGE_KEY = 'image_'
PROBABILITY_KEY = 'probability_'

# This method is called for all the next process steps after start_process()
@require_GET
def get_data(request, server_id):

    # Retrieve image by id
    image = Image.objects.get(pk=server_id)
    if not image:
        return JsonResponse({"Success": False, "Message": "Database error: the requested image doesn't exist anymore"})

    # Ask Processor the Feature detection
    Processor.process(image)
    corresponding_images = CorrespondingImages.objects.filter(base_image=image.id)
    results = []
    for corresponding_image in corresponding_images:
        results.append({
            ID_KEY: 666,
            IMAGE_KEY: base64.encodebytes(bytearray(io.open(image.base_image.path, 'rb').read())).decode(
                'utf-8'),
            PROBABILITY_KEY: random.random()
        })
    if len(results):
        return JsonResponse({"Success": True, "Data": {"ResultImages": results}})
    else:
        return JsonResponse({"Success": False, "Message": "Impossible to recognize anything"})
