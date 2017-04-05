# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class RedtubeItem(scrapy.Item):
    url = Field()
    title = Field()
    depth = Field()

    pornstar_name = Field()
    pornstar_picture = Field()
    pornstar_rank = Field()
    pornstar_total_video = Field()
    pornstar_subscribers = Field()
    pornstar_total_views = Field()
    
    pornstar_video = Field()
    video_title = Field()
    video_views = Field()
    video_rating = Field()
