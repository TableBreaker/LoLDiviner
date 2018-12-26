#coding=utf-8

class SummonerDTO:
    def __init__(self, jsonData):
        self.jsonData = jsonData
        self.profileIconId = jsonData["profileIconId"]
        self.name = jsonData["name"]
        self.puuid = jsonData["puuid"]
        self.summonerLevel = jsonData["summonerLevel"]
        self.revisionDate = jsonData["revisionDate"]
        self.id = jsonData["id"]
        self.accountId = jsonData["accountId"]
        return