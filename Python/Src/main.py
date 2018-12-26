#coding=utf-8
import requests
import json
import sys
import time
import api
from lolData import matchData
from lolData import apiData
from lolData import generatedData

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
    js = open("Resource/" + name + ".json", "w")
    json.dump(obj, js)
    js.close()

if __name__ == "__main__":
    main()