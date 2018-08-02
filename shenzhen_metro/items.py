# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GaodeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    station_num = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    station_name = scrapy.Field()

