#coding=utf-8

class MatchlistDto:
    def __init__(self, jsonData):
        self.jsonData = jsonData
        self.matches = []
        for item in jsonData["matches"]:
            self.matches.append(MatchReferenceDto(item))
        self.totalGames = jsonData["totalGames"]
        self.startIndex = jsonData["startIndex"]
        self.endIndex = jsonData["endIndex"]
        return

class MatchReferenceDto:
    def __init__(self, jsonData):
        self.jsonData = jsonData
        self.lane = jsonData["lane"]
        self.gameId = jsonData["gameId"]
        self.champion = jsonData["champion"]
        self.platformId = jsonData["platformId"]
        self.timestamp = jsonData["timestamp"]
        self.queue = jsonData["queue"]
        self.role = jsonData["role"]
        self.season = jsonData["season"]
        return