#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from requests_oauthlib import OAuth1Session

#SlackのAPI
API_TOKEN = "xoxp-15017424657-15066001425-185420635744-2301e7588b711900ebc5f2425392b3af"
list_url = "https://slack.com/api/users.list"
profile_url = "https://slack.com/api/users.profile.get"

payload = {
    'token' : API_TOKEN,
}

def main():
    GetList()
    #GetProfile()

def GetList():
    res = requests.get(list_url, params = payload)
    member_list = json.loads(res.text)

    for member in member_list['members']:
        if(member['deleted'] == False):
            print(member['profile']['email'])

def GetProfile():
    res = requests.get(profile_url, params=payload)
    member_list = json.loads(res.text)

    for member in member_list['profile']["email"]:
        print(member)

if __name__ == '__main__':
    main()