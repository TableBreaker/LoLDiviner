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
    group = makeGroup(match)
    exportJson(group, "TestGroup")
    return 0

def makeGroup(targetMatch):
    group = generatedData.MatchGroup(targetMatch)
    for item in targetMatch.participantIdentities:
        smGroup = makeSummonerMatchGroup(item.player.accountId)
        group.summonerGroups.append(smGroup)
    
    #print (group.toJson())
    return group

def makeSummonerMatchGroup(accountId):
    summonerjson = api.requestSummonerDataByAccount(accountId)
    smDto = summonerData.SummonerDTO(summonerjson)
    smMatchGroup = generatedData.SummonerMatchGroup(smDto)

    matchListResponse = api.requestMatchList(accountId)
    matchList = matchListData.MatchlistDto(matchListResponse)

    for item in matchList.matches:
        matchJson = api.requestMatchData(item.gameId)
        matchDto = matchData.MatchDto(matchJson)
        smMatchGroup.matchs.append(matchDto)

    return smMatchGroup

def exportJson(obj, name):
    path = "Resource/" + name + ".json"
    file = open(path, "w")
    json.dump(obj, file, default=lambda o: o.__dict__)
    file.close()
    print ("write json file: " + path)

def toJson(obj):
    return json.dumps(obj, default=lambda o: o.__dict__)


if __name__ == "__main__":
    main()