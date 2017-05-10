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
        for i in zip(res.select('.style2 a')[1::2], 地區, 薪資, res.select('.style2 a')[::2]):
            yield scrapy.Request('http://'+self.allowed_domains[0] + i[0]['href'], callback=self.parse_detail,meta={'地區': i[1].text.strip(), '薪資':i[2].text.strip(), 'company':i[3]['title'].split()[0].strip()})

    def parse_detail(self, response):
        res = BeautifulSoup(response.text)
        title = list(map(lambda x:(x.text).replace('：', '').strip(), res.select('#midblock dt'))) + ['url', 'job']
        content = list(map(lambda x:(x.text).replace('：', '').strip(), res.select('#midblock dd'))) + [response.url, res.select('div h1')[0].text.strip()]
        if len(title) != len(content):
            with open('error.log','a') as f:
                f.write(response.url + '\n')
            return
        data = dict(zip(title, content))
        internItem = Crawler1111Item()
        data.update(response.meta)
        for i in internItem.fields.keys():
            internItem.setdefault(i, data.get(i, None))
        return internItem