# -*- coding: utf-8 -*-
import scrapy

# 中国行政区划
class AdministrativedivisionItem(scrapy.Item):
  parentCode = scrapy.Field()
  code = scrapy.Field()
  subCode = scrapy.Field()
  name = scrapy.Field()
  url = scrapy.Field()
