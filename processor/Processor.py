import base64
import io
import json

from numpy import random

ID_KEY = 'Id_'
IMAGE_KEY = 'image_'
PROBABILITY_KEY = 'probability_'


class Processor:

    @staticmethod
    def process(image):
        image.zone_detected_image.save('IMG_' + str(image.id) + '.jpg', image.base_image)
        data = {
            'ResultImages': []
        }
        for i in range(4):
            '''with open(image.zone_detected_image.path, 'rb') as f:'''
            data.get('ResultImages').append({
                ID_KEY: 666 + i,
                IMAGE_KEY: base64.encodebytes(bytearray(io.open(image.zone_detected_image.path, 'rb').read())).decode('utf-8'),
                PROBABILITY_KEY: random.random()
            })
        image.corresponding_data = data
        return True
