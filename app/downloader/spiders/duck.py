import scrapy

from ..items import DuckPictureItem

urls = ['https://www.istockphoto.com/fr/search/more-like-this/155358150?assettype=image&phrase=duck',               # Mallard
        'https://www.istockphoto.com/fr/search/more-like-this/496630422?assettype=image&phrase=duck'                # Mandarin
        'https://www.istockphoto.com/fr/search/more-like-this/172684964?assettype=image&phrase=duck'                # Harlequin
        'https://www.istockphoto.com/fr/search/more-like-this/1264750864?assettype=image&phrase=duck'               # Ruddy
        'https://www.istockphoto.com/fr/search/more-like-this/643723794?assettype=image&phrase=duck'                # Wood
        'https://www.istockphoto.com/fr/search/more-like-this/91813584?assettype=image&phrase=duck'                 # Brown-ish with dots duck, idk the origin
        'https://www.istockphoto.com/fr/search/more-like-this/1092941632?assettype=image&phrase=white%20duck']      # White duck, idk the origin


class DuckSpider(scrapy.Spider):
    name = 'duck'
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
