#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import slack_token

#SlackのAPI
list_url = "https://slack.com/api/users.list"
profile_url = "https://slack.com/api/users.profile.get"

payload = {
    'token' : slack_token.API_TOKEN,
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