### Sample code to submit URLs to Google Index API

Had written this code for a client that needed to tell Google to index some of their URLs via the Google Index API.
There weren't any good examples, so i thought of showing to someone who might need to do it in Python.

###### Installation
1. Bootstrap the dependencies
```
pip install -r requirements.txt
```
2. Set the path of your Google JSON Key crendential file
```
export GOOGLE_KEY_JSON_FILE="/path/of/your/google/json/key/file
```
3. Change `BASE_URL` to your domain (including the trailing slash!)

Then modify the script as you would like.

`submit_urls_batch.py` accesses the API in "batches" of 1000 URLs at one request (Google Index API call limit is 200 requests per day) so i would recommend this rather than `submit_urls.py`

`submit_urls.py` is just there to give an example of how it works. Do not use it! (like i mentioned, if you run this and you have more than 200 URLs and a request for every URL, you will use your daily request quota pretty fast!)
