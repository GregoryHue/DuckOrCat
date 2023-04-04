# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from PIL import Image, UnidentifiedImageError
import requests
from io import BytesIO
import os
import os.path
from .settings import IMAGES_STORE


class Pipeline(object):
    def process_item(self, item, spider):
        error = []
        folder_exists = os.path.exists(IMAGES_STORE)
        if not folder_exists:
            os.makedirs(IMAGES_STORE)
        _, _, files = next(os.walk(IMAGES_STORE))
        i = len(files)
        for image in item['image_urls']:
            try:
                response = requests.get(image)
                img = Image.open(BytesIO(response.content))
                img = img.convert('RGB')
                if img.height > 200 and img.width > 200:
                    path = IMAGES_STORE + '/' + spider.name + '_' + str(i) + '.jpeg'
                    img.save(path, optimize=True, quality=85)
                    i = i + 1
            except UnidentifiedImageError:
                print('error')
                error.append(image)
        print(error)
        return item
