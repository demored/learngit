# -*- coding: utf-8 -*-
import scrapy

from redSpider.items import redspiderItem

class JobPositionSpider(scrapy.Spider):
    name = 'job_position'
    allowed_domains = ['military.people.com.cn']
    start_urls = ['http://military.people.com.cn/']

    def parse(self, response):
        for job_primary in response.xpath('//div[@class="news_box"]'):
            item = redspiderItem()
            item['title'] = job_primary.xpath('./ul/li/a/text()').extract_first()
            yield item
        pass
