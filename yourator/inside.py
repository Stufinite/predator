#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, json
from bs4 import BeautifulSoup
result = json.load(open('intern.json', 'r'))
for i in result:	
	res = requests.get('https://www.yourator.co/'+i['path']).text
	soup = BeautifulSoup(res, "lxml")
	i['inside'] = {}
	i['inside']['description'] = soup.select('.description')[0].text.strip()
	for j in soup.select('.basic-info'):
		key, value = j.text.strip().replace(' ','').replace('\n','').split('：')
		i['inside'][key] = value

with open('finalIntern.json', 'w') as f:
	json.dump(result, f)
