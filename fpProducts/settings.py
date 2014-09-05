# -*- coding: utf-8 -*-

# Scrapy settings for fpProducts project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'fpProducts'

SPIDER_MODULES = ['fpProducts.spiders']
NEWSPIDER_MODULE = 'fpProducts.spiders'
ITEM_PIPELINES = ['fpProducts.pipelines.BankProductPipline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'fpProducts (+http://www.yourdomain.com)'
