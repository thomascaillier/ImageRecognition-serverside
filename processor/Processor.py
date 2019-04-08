import base64
import io
import json

from django.core.files import File
from django.core.files.base import ContentFile
from numpy import random

from app.models import CorrespondingImages

ID_KEY = 'Id_'
IMAGE_KEY = 'image_'
PROBABILITY_KEY = 'probability_'
NUMBER_CORRESPONDING_IMAGES = 3

class Processor:

    @staticmethod
    def process(image):
        from cnn.query_online import analyse_image
        analyseresult = analyse_image(image)
        for i in range(NUMBER_CORRESPONDING_IMAGES):
            img = analyseresult[2*i]
            score = analyseresult[2*i+1]
            print(img, score)
            Image = open("../dataset-retr/train" + "/" + img, "rb")
            imageContent = Image.read()
            Image.close()
            imgb64 = base64.b64encode(imageContent)
            model = CorrespondingImages(base_image=image, score=score)
            model.save()
            model.image.save('IMG_' + str(image.id) + '.jpg', ContentFile(imgb64))
            model.save()
        '''image.zone_detected_image.save('IMG_' + str(image.id) + '.jpg', image.base_image)
        data = {
            'ResultImages': []
        }
        for i in range(4):
            data.get('ResultImages').append({
                ID_KEY: 666 + i,
                IMAGE_KEY: base64.encodebytes(bytearray(io.open(image.zone_detected_image.path, 'rb').read())).decode('utf-8'),
                PROBABILITY_KEY: random.random()
            })
        image.corresponding_data = data'''
        return True
