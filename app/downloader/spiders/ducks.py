import scrapy

from ..items import DuckPictureItem


class DuckSpider(scrapy.Spider):
    name = 'ducks'
    allowed_domains = ['www.unsplash.com']
    start_urls = ['https://unsplash.com/s/photos/duck'] #+ str(i) for i in range(1, 100)]

    def parse(self, response):
        item = DuckPictureItem()
        if response.status == 200:
            rel_img_urls = response.xpath("//img/@src").extract()
            item['image_urls'] = self.url_join(rel_img_urls, response)
        yield item

    def url_join(self, rel_img_urls, response):
        joined_urls = []
        for rel_img_url in rel_img_urls:
            joined_urls.append(response.urljoin(rel_img_url))

        return joined_urls