# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import urllib2
import settings

class UnsplashPipeline(object):
    def __init__(self):
        self.cnt = 1
        dir_path = './pic'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def process_item(self, item, spider):
        for pic_url in item['pic_urls']:
            print pic_url
            pic_name = str(self.cnt)+'.jpg'
            pic = urllib2.urlopen(pic_url).read()
            file = open('./pic/' + pic_name, 'wb')
            file.write(pic)
            file.close()
            self.cnt += 1
        return item
