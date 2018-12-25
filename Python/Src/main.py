#coding=utf-8
import requests
import json
import sys
import data
import time

def main():
    
    return 0

def requestSummonerData(summonerName):
    return None

def requestMasterQueue():
    return None

def requestGrandMasterQueue():
    return None

def requestChallengerQueue():
    return None

def requestMatchData(matchId):
    return None

def requestMatchList(accountId):
    return None

def requestURL(API, param):
    urlFormat = "https://na1.api.riotgames.com{0}{1}?api_key={2}"
    url = urlFormat.format(API, param, data.ApiUrl.APIKEY)
    print ("Request: " + url)
    response = requests.get(url)
    time.sleep(.05)
    return response.json()

if __name__ == "__main__":
    main()