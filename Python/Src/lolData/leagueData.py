#coding=utf-8

class LeagueListDTO:
    def __init__(self, jsonData):
        self.leagueId = jsonData["leagueId"] if "leagueId" in jsonData else None
        self.tier = jsonData["tier"] if "tier" in jsonData else None
        self.entries = []
        if "entries" in jsonData:
            for item in jsonData["entries"]:
                self.entries.append(LeagueItemDTO(item))
        self.queue = jsonData["queue"] if "queue" in jsonData else None
        self.name = jsonData["name"] if "name" in jsonData else None

class LeagueItemDTO:
    def __init__(self, jsonData):
        self.rank = jsonData["rank"] if "rank" in jsonData else None
        self.hotStreak = jsonData["hotStreak"] if "hotStreak" in jsonData else None
        self.miniSeries = MiniSeriesDTO(jsonData["miniSeries"]) if "miniSeries" in jsonData else None
        self.wins = jsonData["wins"] if "wins" in jsonData else None
        self.veteran = jsonData["veteran"] if "veteran" in jsonData else None
        self.losses = jsonData["losses"] if "losses" in jsonData else None
        self.freshBlood = jsonData["freshBlood"] if "freshBlood" in jsonData else None
        self.playerOrTeamName = jsonData["playerOrTeamName"] if "playerOrTeamName" in jsonData else None
        self.inactive = jsonData["inactice"] if "inactive" in jsonData else None
        self.playerOrTeamId = jsonData["playerOrTeamId"] if "playerOrTeamId" in jsonData else None
        self.leaguePoints = jsonData["leaguePoints"] if "leaguePoints" in jsonData else None

class MiniSeriesDTO:
    def __init__(self, jsonData):
        self.wins = jsonData["wins"] if "wins" in jsonData else None
        self.losses = jsonData["losses"] if "losses" in jsonData else None
        self.target = jsonData["target"] if "target" in jsonData else None
        self.progress = jsonData["progress"] if "progress" in jsonData else None