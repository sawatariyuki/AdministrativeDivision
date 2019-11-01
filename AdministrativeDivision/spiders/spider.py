# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
from AdministrativeDivision.items import AdministrativedivisionItem
from scrapy.http import Request
import copy

class ADSpider(scrapy.Spider):
  base_domain_url = 'http://www.stats.gov.cn'
  name = 'spider'
  allowed_domains = ['www.stats.gov.cn']
  start_urls = [
    'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/index.html'
  ]

  # 省级
  def parse(self, response):
    url = urllib.parse.unquote(response.url)
    yearStr1 = url.split('tjsj/tjbz/tjyqhdmhcxhfdm/')
    yearStr2 = yearStr1[1].split('/index.html') if len(yearStr1) == 2 else ''
    year = yearStr2[0] if len(yearStr2) == 2 else ''
    urlMap = {}
    for tr in response.xpath('//table[@class="provincetable"]/tr[@class="provincetr"]'):
      for a in tr.xpath('td/a'):
        href = a.xpath('@href').extract()[0]
        code = href.split('.')[0]
        name = a.xpath('text()').extract()[0]
        item = AdministrativedivisionItem()
        item['parentCode'] = year
        item['code'] = code
        item['name'] = name
        item['url'] = url.replace('index.html', href)
        urlMap[code] = item['url']
        yield item
    for code in urlMap:
      yield Request(url=urlMap[code], meta={'parentCode': code}, callback=self.parse_L1)

  # 地级
  def parse_L1(self, response):
    parentCode = response.meta['parentCode']
    url = urllib.parse.unquote(response.url)
    urlMap = {}
    for tr in  response.xpath('//table[@class="citytable"]/tr[@class="citytr"]'):
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
    for code in urlMap:
      yield Request(url=urlMap[code], meta={'parentCode': code}, callback=self.parse_L2)

  # 县级
  def parse_L2(self, response):
    parentCode = response.meta['parentCode']
    url = urllib.parse.unquote(response.url)
    urlMap = {}
    for tr in  response.xpath('//table[@class="countytable"]/tr[@class="countytr"]'):
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
    for code in urlMap:
      yield Request(url=urlMap[code], meta={'parentCode': code}, callback=self.parse_L3)

  # 乡级
  def parse_L3(self, response):
    parentCode = response.meta['parentCode']
    url = urllib.parse.unquote(response.url)
    urlMap = {}
    for tr in  response.xpath('//table[@class="towntable"]/tr[@class="towntr"]'):
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
    for code in urlMap:
      yield Request(url=urlMap[code], meta={'parentCode': code}, callback=self.parse_L4)

  # 乡下级
  def parse_L4(self, response):
    parentCode = response.meta['parentCode']
    url = urllib.parse.unquote(response.url)
    for tr in  response.xpath('//table[@class="villagetable"]/tr[@class="villagetr"]'):
      tr_tds = tr.xpath('td')
      if len(tr_tds) == 3:
        code = tr_tds[0].xpath('text()').extract()[0]
        subCode = tr_tds[1].xpath('text()').extract()[0]
        name = tr_tds[2].xpath('text()').extract()[0]
        item = AdministrativedivisionItem()
        item['parentCode'] = parentCode
        item['code'] = code
        item['subCode'] = subCode
        item['name'] = name
        yield item