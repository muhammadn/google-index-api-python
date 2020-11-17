### Sample code to submit URLs to Google Index API

Had written this code for a client that needed to tell Google to index their URLs via the Google Index API.
There weren't any good examples, so i thought of showing to someone who might need to do it in Python.

###### Installation
```
pip install -r requirements.txt
```

Then modify the script as you would like.

`submit_urls_batch.py` accesses the API in "batches" of 1000 URLs at one request (limit is 200 requests per day) so i would recommend this ratehr than `submit_urls.py`

`submit_urls.py` is just there to give an example of how it works. Do not use it (like i mentioned, if you run this and you have more than 200 URLs, you will use your quota pretty fast!)