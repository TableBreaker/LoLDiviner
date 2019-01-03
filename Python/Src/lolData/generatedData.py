#coding=utf-8

# class JsonData:
#     def __init__(self):
#         self._jsonData = ""

#     def toJson(self):
#         return self._jsonData

class MatchGroup:
    def __init__(self, targetMatch):
        self.target = targetMatch
        self.summonerGroups = []

class SummonerMatchGroup:
    def __init__(self, summonerData):
        self.summoner = summonerData
        self.matchs = []

# class MatchIDGroup:
#     def __init__(self, targetId):
#         self.targetId = targetId
#         self.summonerIdGroups = []

# class SummonerMatchIDGroup:
#     def __init__(self, accountId):
#         self.accountId = accountId
#         self.matchIds = []