# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from crawler_1111.items import Crawler1111Item

class InternSpider(scrapy.Spider):
    name = "intern"
    allowed_domains = ["www.1111.com.tw"]
    start_urls =  list(map(lambda x:'https://www.1111.com.tw/zone/internships/?page={}&ob=salary'.format(x), range(1,38)))

    def parse(self, response):
        res = BeautifulSoup(response.body)
        學歷, 地區, 薪資 = res.select('.list_black')[::3], res.select('.list_black')[1::3], res.select('.list_black')[2::3]
        for i in zip(res.select('.style2 a')[1::2], 地區, 薪資):
            yield scrapy.Request('http://'+self.allowed_domains[0] + i[0]['href'], callback=self.parse_detail,meta={'地區': i[1].text.strip(), '薪資':i[2].text.strip()})

    def parse_detail(self, response):
        res = BeautifulSoup(response.body)
        title = list(map(lambda x:(x.text).replace('：', '').strip(), res.select('dl dt')))[:16] + ['url', 'job']
        content = list(map(lambda x:(x.text).replace('：', '').strip(), res.select('dl dd')))[:16] + [response.url, res.select('div h1')[0].text.strip()]
        data = dict(zip(title, content))
        internItem = Crawler1111Item()
        internItem['地區'] = response.meta['地區']
        internItem['薪資'] = response.meta['薪資']
        internItem['job'] = data['job']
        internItem['工作時間'] = data.get('工作時間', None)
        internItem['工作性質'] = data.get('工作性質', None)
        internItem['到職日期'] = data.get('到職日期', None)
        internItem['休假制度'] = data.get('休假制度', None)
        # internItem['工作待遇'] = data.get('工作待遇', None)
        internItem['學歷限制'] = data.get('學歷限制', None)
        internItem['工作說明'] = data.get('工作說明', None)
        internItem['職務類別'] = data.get('職務類別', None)
        internItem['科系限制'] = data.get('科系限制', None)
        internItem['聯絡人員'] = data.get('聯絡人員', None)
        internItem['需求人數'] = data.get('需求人數', None)
        internItem['url'] = data['url']
        internItem['身份類別'] = data.get('身份類別', None)
        internItem['工作地點'] = data.get('工作地點', None)
        internItem['實習時段'] = data.get('實習時段', None)
        internItem['工作經驗'] = data.get('工作經驗', None)
        internItem['職缺更新'] = data.get('職缺更新', None)
        return internItem