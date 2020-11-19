from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import csv
import json
import os
from googleapiclient.discovery import build

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

SCOPES = [ "https://www.googleapis.com/auth/indexing" ]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
BASE_URL = "https://example.com/" # base URL to submit the URL, includes trailing slash!

# service_account_file.json is the private key that you created for your service account.
JSON_KEY_FILE = os.environ.get('GOOGLE_KEY_JSON_FILE')

credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)

http = credentials.authorize(httplib2.Http())
service = build('indexing', 'v3', credentials=credentials)

# Define contents here as a JSON string.
# This example shows a simple update request.
# Other types of requests are described in the next step.
urls = []
content_array = []

def callback(request_id, response, exception):
    if exception is not None:
    # Do something with the exception
    #   pass
        print('An exception occurred: ', exception)
    #   pass
        print('request_id is: ', request_id)
        print('response is: ', response)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def process(content):
    urls = list(chunks(content, 1000))
    for x in urls:
        print('Submitting URL to Google Index API in batches of 10000')
        print('Now running ' + str(len(x)) + ' URLs')
        batch = service.new_batch_http_request(callback=callback)
        for y in x:
            postBody = service.urlNotifications().publish(body = y)
            batch.add(postBody)
        batch.execute()
        print('Done!')

with open('city.csv', newline='') as csvfile:
    city = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in city:
        city = row[0].replace(' ', '-').lower()
        for x in languages:
            url = BASE_URL + x + '-tutor-' + city
            urls.append(url)
            content = {"url": url, "type": "URL_UPDATED"}
            content_array.append(content)

process(content_array)

print("Total number of URLs: " + str(len(urls)))
