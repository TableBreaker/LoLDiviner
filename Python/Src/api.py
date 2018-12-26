#coding=utf-8
import json
import requests
import sys
import time
from lolData import matchData
from lolData import apiData

def requestSummonerData(summonerName):
    return None

def requestMasterQueue():
    return None

def requestGrandMasterQueue():
    return None

def requestChallengerQueue():
    return None

def requestMatchData(matchId):
    response = requestURL(apiData.ApiUrl.MATCH_API, matchId)
    return response

def requestMatchList(accountId):
    response = requestURL(apiData.ApiUrl.ACCOUNT_MATCH_LIST_API, accountId)
    return response

def requestURL(API, param):
    urlFormat = "https://na1.api.riotgames.com{0}{1}?api_key={2}"
    url = urlFormat.format(API, param, apiData.APIKEY)
    print ("Request: " + url)
    response = requests.get(url)
    time.sleep(.05)
    return response.json()