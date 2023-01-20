import scrapy

class DuckPictureItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()