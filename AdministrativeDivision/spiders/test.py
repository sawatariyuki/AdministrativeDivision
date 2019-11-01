# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
from AdministrativeDivision.items import AdministrativedivisionItem
from scrapy.http import Request
import copy

class ADSpider(scrapy.Spider):
  base_domain_url = 'http://www.stats.gov.cn'
  name = 'test'
  allowed_domains = ['www.stats.gov.cn']
  start_urls = [
    'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/32.html'
  ]

  # 乡下级
  def parse(self, response):
    parentCode = '13333'
    url = urllib.parse.unquote(response.url)
    urlMap = {}
    for tr in  response.xpath('//table[@class="citytable"]//tr[@class="citytr"]'):
      tr_tds = tr.xpath('td')
      if len(tr_tds) == 2:
        item = AdministrativedivisionItem()
        item['parentCode'] = parentCode
        if len(tr_tds[0].xpath('a')) == 0:
          code = tr_tds[0].xpath('text()').extract()[0]
          name = tr_tds[1].xpath('text()').extract()[0]
          item['code'] = code
          item['name'] = name
        else:
          href = tr_tds[0].xpath('a/@href').extract()[0]
          code = tr_tds[0].xpath('a/text()').extract()[0]
          name = tr_tds[1].xpath('a/text()').extract()[0]
          item['code'] = code
          item['name'] = name
          urlParts = url.split('/')
          urlEnd = urlParts[len(urlParts) - 1]
          item['url'] = url.replace(urlEnd, href)
          urlMap[code] = item['url']
        yield item