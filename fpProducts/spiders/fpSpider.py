
from scrapy.spider import BaseSpider
from scrapy.selector import Selector


class FpSpider(BaseSpider):
    name = "fpSpider"
    allowed_domains = ["cbalicai.com"]
    start_urls = ["http://www.cbalicai.com/producttoIndex.do"]


    def parse(self, response):
        hxs = Selector(response)

        sites = hxs.xpath("/html/body/div/div[2]/div[1]/div/table/tbody/tr")
        for site in sites:
            productName = site.xpath('td[2]/a/@title')[0].extract()
            productDetailURL = site.xpath('td[2]/a/@href')[0].extract()
            bankName = site.xpath("td[3]/text()")[0].extract().strip()
            bizhong = site.xpath('td[4]/text()')[0].extract().strip()
            startDate = site.xpath('td[5]/text()')[0].extract().strip()
            endDate = site.xpath('td[6]/text()')[0].extract().strip()
            managerProid = site.xpath('td[7]/text()')[0].extract().strip()
            mixMoneny = site.xpath('td[8]/text()')[0].extract().strip()
            rate = site.xpath('td[9]/text()')[0].extract().strip()
            incomeType = site.xpath('td[10]/text()')[0].extract().strip()
            buySites = site.xpath('td[11]/text()')[0].extract().strip()

            print("++++++++++++++++++++++++")
            print(productName)
            print(productDetailURL)
            print(bankName)
            print(bizhong)
            print(startDate)
            print(endDate)
            print(managerProid)
            print(mixMoneny)
            print(rate)
            print(incomeType)
            print(buySites)
            print("++++++++++++++++++++++++")


