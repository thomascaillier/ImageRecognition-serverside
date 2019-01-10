
class Processor:

    @staticmethod
    def process(image):
        image.zone_detected_image.save('IMG_' + str(image.id) + '.jpg', image.base_image)
        data = {
            'wikipedia_url': 'https://wikipedia.com/sample',
            'logo': 'https://www.usine-digitale.fr/mediatheque/5/0/0/000305005_homePageUne/logo-google-g.jpg'
        }
        image.corresponding_data = data
        return True

