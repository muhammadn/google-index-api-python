from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import csv
import json

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

# service_account_file.json is the private key that you created for your service account.
JSON_KEY_FILE = os.environ.get('GOOGLE_KEY_JSON_FILE')

credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)

http = credentials.authorize(httplib2.Http())

# Define contents here as a JSON string.
# This example shows a simple update request.
# Other types of requests are described in the next step.
urls = []
with open('city.csv', newline='') as csvfile:
    city = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in city:
        city = row[0].replace(' ', '-').lower()
        for x in languages:
            url = 'https://www.tutoroo.co/' + x + '-tutor-' + city
            print(url)
            urls.append('https://www.tutoroo.co/' + x + '-tutor-' + city)
            content = {"url": url, "type": "URL_UPDATED"}
            content_object = json.dumps(content, indent = 4) 
            response, content = http.request(ENDPOINT, method="POST", body=content_object)
            print(content)

print("number of URLs: " + str(len(urls)))
