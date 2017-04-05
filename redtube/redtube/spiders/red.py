# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from redtube.items import RedtubeItem


class RedSpider(CrawlSpider):
    name = "red"
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
            item['pornstar_picture'] = response.xpath(".//*[@id='contentHolder']/div/div[2]/div[4]/div[1]/img/@src").extract()
            item['pornstar_rank'] = response.xpath(".//*[@id='contentHolder']/div/div[2]/div[4]/div[2]/div/ul/li[1]/text()").extract()
            item['pornstar_total_video'] = response.xpath(".//*[@id='contentHolder']/div/div[2]/div[4]/div[2]/div/ul/li[2]/text()").extract()
            item['pornstar_subscribers'] = response.xpath(".//*[@id='contentHolder']/div/div[2]/div[4]/div[2]/div/ul/li[3]/text()").extract()
            item['pornstar_total_views'] = response.xpath(".//*[@id='contentHolder']/div/div[2]/div[4]/div[2]/div/ul/li[4]/text()").extract()

            return item
