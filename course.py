# -*- coding: utf-8 -*-
from PttWebCrawler import *
import re, json

def contfunc(string):
    needed = re.search('用書(.+?)評分方式',string, re.S).group(1) if re.search('用書(.+?)評分方式',string, re.S)!=None else ''
    exam = re.search('評分方式(.+?)注意事項',string, re.S).group(1) if re.search('評分方式(.+?)注意事項',string, re.S)!=None else ''
    feedback = re.search('注意事項(.+?)成績參考',string, re.S).group(1).replace('心得/結語', '') if re.search('注意事項(.+?)成績參考',string, re.S)!=None else ''
    average = re.search('平均分數(.+?)90',string, re.S).group(1).replace("：", '') if re.search('平均分數(.+?)90',string, re.S)!=None else ''
    if needed == exam == feedback == average == '':
        return string
    return {'book':needed, 'exam':exam, 'feedback':feedback, 'average':average}

def titlefunc(string):
    if '[心得]' in string:
        string = string.replace('[心得] ', '').split('/')
        genra = string[0]
        time = string[1]
        name = string[2]
        teacher = string[3]
        return {'genra':genra, 'time':time, 'name':name, 'teacher':teacher}
    else:
        return string

c = PttWebCrawler('NCHU-Courses',True , start=149, end=150, contentCallback=contfunc, titleCallback=titlefunc)
with open(c.getFilename(), 'r', encoding='utf-8') as f:
    jfile = json.load(f)
    result = list(filter(lambda x:'genra' in x['article_title'], jfile['articles']))
    json.dump(result, open('cleanCourse.json', 'w'))