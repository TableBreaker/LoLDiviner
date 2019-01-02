#coding=utf-8

class MatchlistDto:
    def __init__(self, jsonData):
        #self.jsonData = jsonData
        self.matches = []
        if "matches" in jsonData:
            for item in jsonData["matches"]:
                self.matches.append(MatchReferenceDto(item))
        self.totalGames = jsonData["totalGames"] if "totalGames" in jsonData else None
        self.startIndex = jsonData["startIndex"] if "startIndex" in jsonData else None
        self.endIndex = jsonData["endIndex"] if "endIndex" in jsonData else None
        return

class MatchReferenceDto:
    def __init__(self, jsonData):
        #self.jsonData = jsonData
        self.lane = jsonData["lane"] if "lane" in jsonData else None
        self.gameId = jsonData["gameId"] if "gameId" in jsonData else None
        self.champion = jsonData["champion"] if "champion" in jsonData else None
        self.platformId = jsonData["platformId"] if "platformId" in jsonData else None
        self.timestamp = jsonData["timestamp"] if "timestamp" in jsonData else None
        self.queue = jsonData["queue"] if "queue" in jsonData else None
        self.role = jsonData["role"] if "role" in jsonData else None
        self.season = jsonData["season"] if "season" in jsonData else None
        return