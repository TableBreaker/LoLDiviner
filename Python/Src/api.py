#coding=utf-8
import json
import requests
import sys
import time
from lolData import matchData
from lolData import apiData

def requestSummonerData(summonerName):
    response = requestURL(apiData.ApiUrl.SUMMONER_DATA_API, summonerName)
    return response

def requestSummonerDataByAccount(accountId):
    response = requestURL(apiData.ApiUrl.SUMMONER_DATA_BY_ACCOUNT_API, accountId)
    return response

def requestMasterQueue():
    response = requestURL(apiData.ApiUrl.MASTER_LEAGUE_API, apiData.ApiParam.SOLORANK)
    return response

def requestGrandMasterQueue():
    response = requestURL(apiData.ApiUrl.GRANDMASTER_LEAGUE_API, apiData.ApiParam.SOLORANK)
    return response

def requestChallengerQueue():
    response = requestURL(apiData.ApiUrl.CHALLENGER_LEAGUE_API, apiData.ApiParam.SOLORANK)
    return response

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