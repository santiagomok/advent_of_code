#!/usr/bin/env python3

from lxml import html
import requests

html = requests.get('https://adventofcode.com/2019/day/1/input').text
print(html)
#  page = requests.get('https://adventofcode.com/2019/day/1/input')
#  tree = html.fromstring(page.content)

#  #  /html/body/pre
#  #  data = tree.xpath('/html/body')
#  data = tree.xpath('//body/*')
#  print(data)
