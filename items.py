# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AH_Product(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    price=scrapy.Field()
    category1=scrapy.Field()
    category2=scrapy.Field()
    category3=scrapy.Field()
    category4=scrapy.Field()
    category5=scrapy.Field()
    unit=scrapy.Field()

