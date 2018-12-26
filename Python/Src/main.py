#coding=utf-8
import requests
import json
import sys
import time
import api
from lolData import matchData, apiData, generatedData, matchListData, summonerData

def main():
    res = api.requestMatchData(2938928303)
    match = matchData.MatchDto(res)
    exportJson(match.jsonData, "test")
    #group = makeGroup(match)
    
    return 0

def makeGroup(targetMatch):
    group = generatedData.MatchGroup(targetMatch)
    return group

def exportJson(obj, name):
    path = "Resource/" + name + ".json"
    js = open(path, "w")
    json.dump(obj, js)
    js.close()
    print ("write json file: " + path)

if __name__ == "__main__":
    main()