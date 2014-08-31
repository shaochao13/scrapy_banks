# -*- coding: utf-8 -*-
__author__ = 'zsc'

from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.http import Request


class BankPoints(BaseSpider):
    name = 'bpSpider'
    allowed_domains = ["cngold.org"]
    start_urls = ["http://bank.cngold.org/yhwd/"]

    def parse(self, response):
        hxs = Selector(response)

        sites = hxs.xpath('//div[@class="num"]/a/@href').extract()

        for url in sites:
            yield Request(url, callback=self.parse_two)

    def parse_two(self, response):
        hxs = Selector(response)
        sites = hxs.xpath('//div[@class="row"]/span/a/@href').extract()

        for url in sites:
            yield Request(url, callback=self.parse_three)

    def parse_three(self, response):
        hxs = Selector(response)
        sites = hxs.xpath('//div[@class="city"]/strong/a/@href').extract()

        for url in sites:
            yield Request(url, callback=self.parse_four)

    def parse_four(self, response):
        hxs = Selector(response)
        sites = hxs.xpath('//ul[@class="wdList"]/li')

        bankName = hxs.xpath('//div[@class="head_site"]/div[@class="site"]/a[3]/text()').extract()[0]
        #print(bankName)

        moreSites = hxs.xpath('//ul[@class="wdPage"]/span/a')
        for site in moreSites:
            text = site.xpath('text()')[0].extract().strip()
            print(text)
            if text == u"下一页":
                url = site.xpath('@href')[0].extract()
                print("+++++++++++++++++  %s", url)
                yield Request(url, callback=self.parse_four)

        for site in sites:
            name = site.xpath('h3/a/@title').extract()[0]
            address = site.xpath('div[@class="xx clearfix"]/div[1]/span/text()').extract()[0]
            phone = site.xpath('div[@class="xx clearfix"]/div[2]/span/text()').extract()[0]




