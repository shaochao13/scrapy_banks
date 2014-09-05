# -*- coding: utf-8 -*-
__author__ = 'zsc'

from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.http import Request
from fpProducts.items import BankPointItem


class BankPoints(BaseSpider):
    name = 'bpSpider'
    allowed_domains = ["cngold.org"]
    start_urls = ["http://bank.cngold.org/yhwd/"]

    def parse(self, response):
        hxs = Selector(response)

        sites = hxs.xpath('//div[@class="num"]/a/@href').extract()
        #sites = [u'http://bank.cngold.org/yhwd/index_5.html']

        for url in sites:
            yield Request(url, callback=self.parse_two)

    def parse_two(self, response):
        hxs = Selector(response)
        sites = hxs.xpath('//div[@class="row"]/span/a/@href').extract()
        #sites = [u'http://bank.cngold.org/yhwd/list_city_5_13.html']
        for url in sites:
            yield Request(url, callback=self.parse_three)

    def parse_three(self, response):
        print("three")
        hxs = Selector(response)
        sites = hxs.xpath('//div[@class="city"]/a/@href').extract()

        for url in sites:
            yield Request(url, callback=self.parse_four)

    def parse_four(self, response):
        hxs = Selector(response)
        sites = hxs.xpath('//ul[@class="wdList"]/li')

        bankName = hxs.xpath('//div[@class="head_site"]/div[@class="site"]/a[3]/text()')[0].extract()
        pointAddress = hxs.xpath('//div[@class="head_site"]/div[@class="site"]/a[4]/text()')[0].extract()
        print("_____________%s________________" % pointAddress)


        for site in sites:

            name = site.xpath('h3/a/@title').extract()[0]
            address = site.xpath('div[@class="xx clearfix"]/div[1]/span/text()').extract()[0]
            phone = site.xpath('div[@class="xx clearfix"]/div[2]/span/text()').extract()[0]

            point = BankPointItem()
            point["bankName"] = bankName
            point["pointName"] = name
            point["address"] = address
            point["phone"] = phone
            point["province"] = pointAddress.split()[0]
            point["city"] = pointAddress.split()[1]

            #url = site.xpath('h3/a/@href').extract()[0]
            #yield Request(url, callback=self.parse_five)
            yield self.parse_five(point)

        moreSites = hxs.xpath('//div[@class="wdPage"]/div[@class="digg"]/span/a')
        for site in moreSites:
            text = site.xpath('text()')[0].extract().strip()
            if text == u"下一页":
                url = site.xpath('@href')[0].extract()
                yield Request(url, callback=self.parse_four)


    def parse_five(self, bpItem):
        '''hxs = Selector(response)
        name = hxs.xpath('//div[@class="bankIntro clearfix"]/h3/a/@title')[0].extract()
        bankName = hxs.xpath('//div[@class="bankIntro clearfix"]/a/img/@alt')[0].extract()
        address = hxs.xpath('//div[@class="info_wd mt-1"]/table/tbody/tr[1]/td[1]/text()')[0].extract()
        phone = hxs.xpath('//div[@class="info_wd mt-1"]/table/tbody/tr[1]/td[2]/text()')[0].extract()


        bpItem = BankPointItem()

        bpItem['bankName'] = bankName
        bpItem['address'] = address
        bpItem['phone'] = phone
        bpItem['pointName'] = name'''

        return bpItem
        #print(name)








