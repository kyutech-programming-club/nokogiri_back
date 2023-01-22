import json
import time
import firebase_admin
from firebase_admin import credentials
from flask import Flask, request, render_template
from firebase_admin import firestore
import requests
from time import sleep

cred = credentials.Certificate("./nokogiri-cup-firebase-adminsdk-6dfx7-6437488830.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

token = "ff1f8f5bc9a2290b3ff7df2cd98a72b8cb4ab32a"

userInformation = db.collection("userInformation")
docs = userInformation.stream()

header = {"Authentication": f"Bearer {token}"}


def callApi(i, id, header):
    url = (
        f"https://qiita.com/api/v2/items?page={i}&per_page=100&query=qiita+user%3A{id}"
    )
    res = requests.get(url, headers=header)
    # if res.json:
    #     return 0
    print(res.json())
    # for k in res.json():
    #     print(k)
    #     time.sleep(2)
    #     # print(k["url"])


idList = []
# for doc in docs:
#     idList.append(doc.to_dict()["id"])


id = "tanacchi"
for i in range(1, 11):
    callApi(i, id, header)
