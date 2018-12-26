#coding=utf-8
import json

class JsonData:
    def __init__(self):
        self._jsonData = ""

    def toJson(self):
        return self._jsonData

class MatchGroup(JsonData):
    def __init__(self, targetMatch):
        self.target = targetMatch
        self.matchGroup = []
    
    def toJson(self):
        return self._jsonData

class SummonerMatchGroup(JsonData):
    def __init__(self, summonerData):
        self.summoner = summonerData
        self.smMatchGroup = []

    def toJson(self):
        return self._jsonData