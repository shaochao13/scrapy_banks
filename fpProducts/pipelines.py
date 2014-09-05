# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import MySQLdb


class BankProductPipline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host="10.1.1.32", user="root", passwd="101132", db="sampledb", charset="utf8")
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):

        try:
            sql = """INSERT INTO `tbl_bank_product_eastmoney`
                        (`productID`, `productName`, `bankName`,
                        `publishCitys`, `currency`, `rate`,
                        `sellStartDate`,  `sellEndDate`, `mixSellAmount`,
                        `sellAmountTimes`,`managerPeriod`, `isBreakEven`,
                        `investWay`,  `productType`,  `incomeType`,
                        `isBankStop`,  `isCustomerRedeem`,  `incomeMethod`,
                        `bankStopCondition`,  `riskPrompt`)
                        VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                        '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" %  ( item["productID"],
                                    item["productName"],
                                    item["bankName"],
                                    item["publishCitys"],
                                    item["currency"],
                                    item["rate"],
                                    item["sellStartDate"],
                                    item["sellEndDate"],
                                    item["mixSellAmount"],
                                    item["sellAmountTimes"],
                                    item["managerPeriod"],
                                    item["isBreakEven"],
                                    item["investWay"],
                                    item["productType"],
                                    item["incomeType"],
                                    item["isBankStop"],
                                    item["isCustomerRedeem"],
                                    item["incomeMethod"],
                                    item["bankStopCondition"],
                                    item["riskPrompt"] )

            self.cursor.execute(sql)
            self.conn.commit()

        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])

        return item



class MysqlStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host="10.1.1.32", user="root", passwd="101132", db="sampledb", charset="utf8")
        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):

        try:
            sql = """INSERT INTO `tbl_bankoutlets`
                        (`bankName`,
                        `address`,
                        `phone`,
                        `outletName`,
                        `province`,
                        `city`,
                        `lat`,
                        `lng`)
                        VALUES
                        """ % (item["bankName"],
                                             item["address"],
                                             item["phone"],
                                             item["pointName"],
                                             item["province"],
                                             item["city"]
                                            )
            self.cursor.execute(sql)
            self.conn.commit()

        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])

        return item

