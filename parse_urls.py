#!/usr/bin/env python

import csv
languages = [
  'english',
  'spanish',
  'french',
  'chinese-mandarin',
  'italian',
  'arabic',
  'russian',
  'portuguese',
  'korean',
  'japanese',
  'thai',
  'german',
  'hebrew',
  'danish',
  'swedish',
  'czech',
]

urls = []
BASE_URL = "https://example.com/" # base URL to submit the URL

with open('city.csv', newline='') as csvfile:
    city = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in city:
        city = row[0].replace(' ', '-').lower()
        for x in languages:
            url = BASE_URL + x + '-tutor-' + city
            print(url)
            urls.append(url)
print("number of URLs: " + str(len(urls)))
