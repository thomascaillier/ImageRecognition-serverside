from django.core.files.base import ContentFile

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
            model = CorrespondingImages(base_image=image, score=score)
            model.save()
            model.image.save('IMG_' + str(image.id) + '.jpg', ContentFile(imageContent))
            model.save()
        return True
