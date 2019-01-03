#coding=utf-8
import requests
import json
import sys
import time
import api
from lolData import matchData, apiData, generatedData, matchListData, summonerData, leagueData

def main():
    targetId = 2938928303
    res = api.requestMatchData(targetId)
    match = matchData.MatchDto(res)
    group = makeGroup(match)
    exportJson(group, "MatchGroup" + str(targetId))

def makeLeagueGroup(leagueListDto):
    return

def makeGroup(targetMatch):
    group = generatedData.MatchGroup(targetMatch)
    for item in targetMatch.participantIdentities:
        print ("Make summoner data ID: " + str(item.participantId))
        smGroup = makeSummonerMatchGroup(item.player.accountId, targetMatch.gameId)
        group.summonerGroups.append(smGroup)

    return group

def makeSummonerMatchGroup(accountId, targetMatchId):
    summonerjson = api.requestSummonerDataByAccount(accountId)
    smDto = summonerData.SummonerDTO(summonerjson)
    smMatchGroup = generatedData.SummonerMatchGroup(smDto)

    matchListResponse = api.requestMatchList(accountId)
    matchList = matchListData.MatchlistDto(matchListResponse)

    index = 0
    start = False
    for item in reversed(matchList.matches):
        if item.gameId == targetMatchId:
            start = True
            continue

        if not start:
            continue
        
        matchJson = api.requestMatchData(item.gameId)
        matchDto = matchData.MatchDto(matchJson)
        matchDto.processMatchData(accountId)
        smMatchGroup.matchs.append(matchDto)
        index += 1
        if index >= 10:
            break

    return smMatchGroup

# def  makeIdGroup(targetId):
#     idGroup = generatedData.MatchIDGroup(targetId)
#     res = api.requestMatchData(targetId)
#     match = matchData.MatchDto(res)
#     for ()
#     return idGroup

# def makeSummonerMatchIdGroup(accountId, targetId):
#     smidGroup = generatedData.SummonerMatchIDGroup(accountId)
#     return smidGroup

def exportJson(obj, name):
    path = "Resource/" + name + ".json"
    file = open(path, "w")
    json.dump(obj, file, default = lambda o: o.__dict__, indent = 4)
    file.close()
    print ("write json file: " + path)

def toJson(obj):
    return json.dumps(obj, default = lambda o: o.__dict__, indent = 4)


if __name__ == "__main__":
    main()