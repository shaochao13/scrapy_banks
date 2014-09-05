# -*- coding: utf-8 -*-
__author__ = 'zsc'

from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.http import Request
from fpProducts.items import BankProductItem
import time

class EastMoneyBankProductSpider(BaseSpider):
    name = 'eastmoneySpider'
    allowed_domains = ["eastmoney.com"]
    start_urls = [u"http://data.eastmoney.com/money/FinancialProducts.aspx?area=&cid=-1&cname=&cuir=1&bt=-1&sale=1&tp=-1&ss=1:false&p=1&ps=25"]

    def parse(self, response):
        hxs = Selector(response)

        sites = hxs.xpath('//tbody[@id="contTbody"]/tr/td[1]/input[@type="checkbox"]/@value').extract()

        for p_id in sites:

            time.sleep(5)

            pid = p_id.split("#")[0]
            url = 'http://data.eastmoney.com/money/FinancialCompare.aspx?id=573863,%s' % pid
            yield Request(url, callback=self.parse_two)

        pagers = hxs.xpath('//div[@id="pager"]/a').extract()
        for site in pagers:
            text = site.xpath('text()')[0].extract().strip()
            if text == u"下一页":
                url = site.xpath('@href')[0].extract()
                yield Request(url, callback=self.parse)

    def parse_two(self, response):
        hxs = Selector(response)

        productID = hxs.xpath('//table[@id="dataTable"]/thead/tr[1]/th[3]/a/@href').extract()[0].split("=")[1]
        productName = hxs.xpath('//table[@id="dataTable"]/thead/tr[1]/th[3]/a/text()').extract()[0]
        bankName = hxs.xpath('//tbody[@id="baseInfoData"]/tr[1]/td[3]/text()').extract()[0]
        publishCitys = hxs.xpath('//tbody[@id="baseInfoData"]/tr[2]/td[3]/text()').extract()[0]
        currency = hxs.xpath('//tbody[@id="baseInfoData"]/tr[3]/td[3]/text()').extract()[0]
        rate = hxs.xpath('//tbody[@id="baseInfoData"]/tr[4]/td[3]/text()').extract()[0]
        sellStartDate = hxs.xpath('//tbody[@id="baseInfoData"]/tr[5]/td[3]/text()').extract()[0]
        sellEndDate = hxs.xpath('//tbody[@id="baseInfoData"]/tr[6]/td[3]/text()').extract()[0]
        mixSellAmount = hxs.xpath('//tbody[@id="baseInfoData"]/tr[7]/td[3]/text()').extract()[0]
        sellAmountTimes = hxs.xpath('//tbody[@id="baseInfoData"]/tr[8]/td[3]/text()').extract()[0]
        managerPeriod = hxs.xpath('//tbody[@id="baseInfoData"]/tr[9]/td[3]/text()').extract()[0]
        isBreakEven = hxs.xpath('//tbody[@id="baseInfoData"]/tr[10]/td[3]/text()').extract()[0]

        investWay = hxs.xpath('//tbody[@id="incomeInfoData"]/tr[1]/td[3]/text()').extract()
        productType = hxs.xpath('//tbody[@id="incomeInfoData"]/tr[2]/td[3]/text()').extract()[0]
        incomeType = hxs.xpath('//tbody[@id="incomeInfoData"]/tr[3]/td[3]/text()').extract()[0]
        isBankStop = hxs.xpath('//tbody[@id="incomeInfoData"]/tr[4]/td[3]/text()').extract()[0]
        isCustomerRedeem = hxs.xpath('//tbody[@id="incomeInfoData"]/tr[5]/td[3]/text()').extract()[0]
        incomeMethod = hxs.xpath('//tbody[@id="incomeInfoData"]//td[18]/text()').extract()

        bankStopCondition = hxs.xpath('//tbody[@id="incomeInfoData"]//td[19]/text()').extract()
        riskPrompt = hxs.xpath('//tbody[@id="incomeInfoData"]//td[20]/text()').extract()

        item = BankProductItem()
        item['productID'] = productID
        item['productName'] = productName
        item['bankName'] = bankName
        item['publishCitys'] = publishCitys
        item['currency'] = currency
        item['rate'] = rate.split("%")[0]
        item['sellStartDate'] = sellStartDate
        item['sellEndDate'] = sellEndDate
        item['mixSellAmount'] = mixSellAmount
        item['sellAmountTimes'] = sellAmountTimes
        item['managerPeriod'] = managerPeriod
        item['isBreakEven'] = isBreakEven
        if len(investWay) > 0:
            item['investWay'] = investWay[0]
        item['productType'] = productType
        item['incomeType'] = incomeType
        item['isBankStop'] = isBankStop
        item['isCustomerRedeem'] = isCustomerRedeem
        if len(incomeMethod)>0:
            item['incomeMethod'] = incomeMethod[0]
        if len(bankStopCondition) >0:
            item['bankStopCondition'] = bankStopCondition
        if len(riskPrompt) >0:
            item['riskPrompt'] = riskPrompt[0]

        return item
