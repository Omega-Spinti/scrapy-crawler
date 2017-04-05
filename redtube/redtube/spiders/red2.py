# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from redtube.items import RedtubeItem


class RedSpider(CrawlSpider):
    name = "red2"
    allowed_domains = ["redtube.com"]
    start_urls = ['http://redtube.com/']
    rules = [
        Rule(LinkExtractor(allow=('\/pornstar')),callback ="parse_page", follow=True)
    ]

    def parse_page(self, response):
        
        summarys = response.xpath("//html")
        item = RedtubeItem()
        
        for summary in summarys:
            
            #page depth
            item['depth'] = response.meta["depth"]
            item['url'] = response.url
            
            #pornstar info
            item['pornstar_name'] = response.xpath(".//*[@id='contentHolder']/div/div[2]/div[4]/div[1]/span/h2/text()").extract()

            #pornstar videos
            item['pornstar_video'] = summary.xpath(".//*[@id='contentHolder']/div/div[2]/ul/li/span[1]/a/@href").extract()
            item['video_title'] = summary.xpath(".//*[@id='contentHolder']/div/div[2]/ul/li/span[1]/a/@title").extract()
            item['video_views'] = summary.xpath(".//*[@id='contentHolder']/div/div[2]/ul/li/span[3]/text()").extract()
            item['video_rating'] = summary.xpath(".//*[@id='contentHolder']/div/div[2]/ul/li/span[2]/text()").extract()
            
            return item
