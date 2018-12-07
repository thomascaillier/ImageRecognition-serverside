import base64
from django.core.files import File

from app.models import Image
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from processor.Processor import Processor


# This method is called for initiate the process sending the image to proceed
@csrf_exempt
@require_POST
def start_process(request):

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
        return JsonResponse({"Success": True, "Key": image.id})
    else:
        image.delete()
        return JsonResponse({"Success": False})


# This method is called for all the next process steps after start_process()
@require_GET
def get_result(request, server_id, step):

    # Retrieve image by id
    image = Image.objects.get(pk=server_id)
    if not image:
        return JsonResponse({"Success": False, "Message": "Database error: the requested image doesn't exist anymore"})

    # Behaviours according to step
    if step == 1:
        # Ask Processor the Feature detection
        Processor.detect_areas(image)
        image.save()
        if image.zone_detected_image:
            with open(image.zone_detected_image.path, "rb") as imageFile:
                encoded_image = base64.b64encode(imageFile.read()).decode("utf-8")
                return JsonResponse({"Success": True, "Data": encoded_image})
        else:
            return JsonResponse({"Success": False, "Message": "Impossible to detect areas"})
    elif step == 2:
        # Ask Processor data corresponding to previously detected areas
        Processor.detect_corresponding_data(image)
        image.save()
        if image.corresponding_data:
            return JsonResponse({"Success": True, "Data": image.corresponding_data})
        else:
            return JsonResponse({"Success": False, "Message": "Impossible to recognize anything"})
