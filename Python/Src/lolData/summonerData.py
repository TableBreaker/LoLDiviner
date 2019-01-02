#coding=utf-8

class SummonerDTO:
    def __init__(self, jsonData):
        #self.jsonData = jsonData
        self.profileIconId = jsonData["profileIconId"] if "profileIconId" in jsonData else None
        self.name = jsonData["name"] if "name" in jsonData else None
        self.puuid = jsonData["puuid"] if "puuid" in jsonData else None
        self.summonerLevel = jsonData["summonerLevel"] if "summonerLevel" in jsonData else None
        self.revisionDate = jsonData["revisionDate"] if "revisionDate" in jsonData else None
        self.id = jsonData["id"] if "id" in jsonData else None
        self.accountId = jsonData["accountId"] if "accountId" in jsonData else None
        return