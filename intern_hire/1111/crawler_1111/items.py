# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Crawler1111Item(scrapy.Item):
    # define the fields for your item here like:    
    job = scrapy.Field()
    company = scrapy.Field()
    url = scrapy.Field()
    地區 = scrapy.Field()
    薪資 = scrapy.Field()
    工作時間 = scrapy.Field()
    工作性質 = scrapy.Field()
    工作待遇 = scrapy.Field()
    工作說明 = scrapy.Field()
    工作經驗 = scrapy.Field()
    實習時段 = scrapy.Field()
    休假制度 = scrapy.Field()
    學歷限制 = scrapy.Field()
    職務類別 = scrapy.Field()
    科系限制 = scrapy.Field()
    需求人數 = scrapy.Field()
    身份類別 = scrapy.Field()
    語言能力 = scrapy.Field()
    電腦專長 = scrapy.Field()
    附加條件 = scrapy.Field()
    專業憑證 = scrapy.Field()
    到職日期 = scrapy.Field()
    職缺更新 = scrapy.Field()