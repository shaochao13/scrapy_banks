# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BankPointItem(scrapy.Item):
    bankName = scrapy.Field()
    pointName = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()


class BankProductItem(scrapy.Item):
    productID = scrapy.Field()
    productName = scrapy.Field()
    bankName = scrapy.Field()
    publishCitys = scrapy.Field()
    currency = scrapy.Field()
    rate = scrapy.Field()
    sellStartDate = scrapy.Field()
    sellEndDate = scrapy.Field()
    mixSellAmount = scrapy.Field()
    sellAmountTimes = scrapy.Field()
    managerPeriod = scrapy.Field()
    isBreakEven = scrapy.Field()

    investWay = scrapy.Field()
    productType = scrapy.Field()
    incomeType = scrapy.Field()
    isBankStop = scrapy.Field()
    isCustomerRedeem = scrapy.Field()
    incomeMethod = scrapy.Field()

    bankStopCondition = scrapy.Field()
    riskPrompt = scrapy.Field()
