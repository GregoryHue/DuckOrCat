import scrapy

from ..items import DuckPictureItem

urls = ['https://www.istockphoto.com/fr/search/more-like-this/171583931?assettype=image&phrase=cat',                # Persian
        'https://www.istockphoto.com/fr/search/more-like-this/1417420135?assettype=image&phrase=cat'                # York Chocolate
        'https://www.istockphoto.com/fr/search/more-like-this/491679239?assettype=image&phrase=cat'                 # Tonkinese
        'https://www.istockphoto.com/fr/search/more-like-this/1145889109?assettype=image&phrase=cat'                # British Shorthair
        'https://www.istockphoto.com/fr/search/more-like-this/523015577?assettype=image&phrase=cat'                 # Somali
        'https://www.istockphoto.com/fr/search/more-like-this/1071204136?assettype=image&phrase=cat'                # Toyger
        'https://www.istockphoto.com/fr/search/more-like-this/623368092?assettype=image&phrase=cat']                # Birman

class DuckSpider(scrapy.Spider):
    name = 'cat'
    allowed_domains = ['www.unsplash.com']
    start_urls = [ j + '&page=' + str(i) for j in urls for i in range(1, 100)]
    

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