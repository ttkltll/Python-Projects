from scrapy.spiders import BaseSpider
import scrapy
import json
import re
from unsplash.items import UnsplashItem
class PictureSpider(scrapy.spiders.Spider):
    name = "picture"
    allowed_domains = ["unsplash.com"]
    start_urls = [
        "https://api.unsplash.com/napi/feeds/home"
    ]

    def parse(self, response):
        item = UnsplashItem()
        res = response.body
        hjson = json.loads(res)
        next_page = hjson[u'next_page']
        pattern = re.compile('after=(.*)')
        page_bianhao = re.findall(pattern, next_page)[0]
        page_url = 'https://api.unsplash.com/napi/feeds/home?after=' + page_bianhao
        print page_url
        photos = hjson[u'photos']
        pic_urls=[]
        for each in photos:
            bianhao = each['id']
            pic_urls.append('https://unsplash.com/photos/' + bianhao + '/download?force=true')
        item['pic_urls']=pic_urls
        print item['pic_urls']
        yield item
        yield scrapy.Request(page_url, callback=self.parse)