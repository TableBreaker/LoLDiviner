#coding = utf-8
import json

class MatchDto:
    def __init__(self, jsonData):
        self.jsonData = jsonData
        self.seasonId = jsonData["seasonId"]
        self.queueId = jsonData["queueId"]
        self.gameId = jsonData["gameId"]
        self.participantIdentities = []
        for item in jsonData["participantIdentities"]:
            self.participantIdentities.append(ParticipantIdentityDto(item))
        self.gameVersion = jsonData["gameVersion"]
        self.platformId = jsonData["platformId"]
        self.gameMode = jsonData["gameMode"]
        self.mapId = jsonData["mapId"]
        self.gameType = jsonData["gameType"]
        self.teams = []
        for item in jsonData["teams"]:
            self.teams.append(TeamStatsDto(item))
        self.participants = []
        for item in jsonData["participants"]:
            self.participants.append(ParticipantDto(item))
        self.gameDuration = jsonData["gameDuration"]
        self.gameCreation = jsonData["gameCreation"]
        
        
class ParticipantIdentityDto:
    def __init__(self, jsonData):
        self.jsonData = jsonData
        self.player = PlayerDto(jsonData["player"])
        self.participantId = jsonData["participantId"]
        return

class PlayerDto:
    def __init__(self, jsonData):
        self.jsonData = jsonData
        self.currentPlatformId = jsonData["currentPlatformId"]
        self.summonerName = jsonData["summonerName"]
        self.matchHistoryUri = jsonData["matchHistoryUri"]
        self.platformId = jsonData["platformId"]
        self.currentAccountId = jsonData["currentAccountId"]
        self.profileIcon = jsonData["profileIcon"]
        self.summonerId = jsonData["summonerId"]
        self.accountId = jsonData["accountId"]
        return

class TeamStatsDto:
    def __init__(self, jsonData):
        self.jsonData = jsonData
        self.firstDragon = jsonData["firstDragon"]
        self.firstInhibitor = jsonData["firstInhibitor"]
        self.bans = []
        for item in jsonData["bans"]:
            self.bans.append(TeamBansDto(item))
        self.baronKills = jsonData["baronKills"]
        self.firstRiftHerald = jsonData["firstRiftHerald"]
        self.firstBaron = jsonData["firstBaron"]
        self.riftHeraldKills = jsonData["riftHeraldKills"]
        self.firstBlood = jsonData["firstBlood"]
        self.teamId = jsonData["teamId"]
        self.firstTower = jsonData["firstTower"]
        self.vilemawKills = jsonData["vilemawKills"]
        self.inhibitorKills = jsonData["inhibitorKills"]
        self.towerKills = jsonData["towerKills"]
        self.dominionVictoryScore = jsonData["dominionVictoryScore"]
        self.win = jsonData["win"]
        self.dragonKills = jsonData["dragonKills"]
        return

class TeamBansDto:
    def __init__(self, jsonData):
        self.jsonData = jsonData
        self.pickTurn = jsonData["pickTurn"]
        self.championId = jsonData["championId"]
        return

class ParticipantDto:
    def __init__(self, jsonData):
        self.jsonData = jsonData
        self.stats = ParticipantStatsDto(jsonData["stats"])
        self.participantId = jsonData["participantId"]
        self.runes = []
        #for item in jsonData["runes"]:
        #    self.runes.append(RuneDto(item))
        self.timeline = ParticipantTimelineDto(jsonData["timeline"])
        self.teamId = jsonData["teamId"]
        self.spell2Id = jsonData["spell2Id"]
        self.masteries = []
        #for item in jsonData["masteries"]:
        #    self.masteries.append(MasteryDto(item))
        self.highestAchievedSeasonTier = jsonData["highestAchievedSeasonTier"]
        self.spell1Id = jsonData["spell1Id"]
        self.championId = jsonData["championId"]
        return

class ParticipantStatsDto:
    def __init__(self, jsonData):
        self.jsonData = jsonData
        self.firstBloodAssist = jsonData["firstBloodAssist"]	
        self.visionScore = jsonData["visionScore"]
        self.magicDamageDealtToChampions = jsonData["magicDamageDealtToChampions"]	
        self.damageDealtToObjectives = jsonData["damageDealtToObjectives"]	
        self.totalTimeCrowdControlDealt = jsonData["totalTimeCrowdControlDealt"]
        self.longestTimeSpentLiving = jsonData["longestTimeSpentLiving"]	
        self.perk1Var1 = jsonData["perk1Var1"]
        self.perk1Var3 = jsonData["perk1Var3"]
        self.perk1Var2 = jsonData["perk1Var2"]
        self.tripleKills = jsonData["perk1Var2"]
        self.perk3Var3 = jsonData["perk3Var3"]
        #self.nodeNeutralizeAssist = jsonData["nodeNeutralizeAssist"]
        self.perk3Var2 = jsonData["perk3Var2"]
        self.playerScore9 = jsonData["playerScore9"]
        self.playerScore8 = jsonData["playerScore8"]
        self.kills = jsonData["kills"]
        self.playerScore1 = jsonData["playerScore1"]
        self.playerScore0 = jsonData["playerScore0"]
        self.playerScore3 = jsonData["playerScore3"]
        self.playerScore2 = jsonData["playerScore2"]
        self.playerScore5 = jsonData["playerScore5"]
        self.playerScore4 = jsonData["playerScore4"]
        self.playerScore7 = jsonData["playerScore7"]
        self.playerScore6 = jsonData["playerScore6"]
        self.perk5Var1 = jsonData["perk5Var1"]
        self.perk5Var3 = jsonData["perk5Var3"]
        self.perk5Var2 = jsonData["perk5Var2"]
        self.totalScoreRank = jsonData["totalScoreRank"]
        self.neutralMinionsKilled = jsonData["neutralMinionsKilled"]
        self.damageDealtToTurrets = jsonData["damageDealtToTurrets"]
        self.physicalDamageDealtToChampions = jsonData["physicalDamageDealtToChampions"]
        #self.nodeCapture = jsonData["nodeCapture"]
        self.largestMultiKill = jsonData["largestMultiKill"]
        self.perk2Var2 = jsonData["perk2Var2"]
        self.perk2Var3 = jsonData["perk2Var3"]
        self.totalUnitsHealed = jsonData["totalUnitsHealed"]
        self.perk2Var1 = jsonData["perk2Var1"]
        self.perk4Var1 = jsonData["perk4Var1"]
        self.perk4Var2 = jsonData["perk4Var2"]
        self.perk4Var3 = jsonData["perk4Var3"]
        self.wardsKilled = jsonData["wardsKilled"]
        self.largestCriticalStrike = jsonData["largestCriticalStrike"]
        self.largestKillingSpree = jsonData["largestKillingSpree"]
        self.quadraKills = jsonData["quadraKills"]
        #self.teamObjective = jsonData["teamObjective"]
        self.magicDamageDealt = jsonData["magicDamageDealt"]	
        self.item2 = jsonData["item2"]
        self.item3 = jsonData["item3"]
        self.item0 = jsonData["item0"]
        self.neutralMinionsKilledTeamJungle = jsonData["neutralMinionsKilledTeamJungle"]
        self.item6 = jsonData["item6"]
        self.item4 = jsonData["item4"]
        self.item5 = jsonData["item5"]
        self.perk1 = jsonData["perk1"]
        self.perk0 = jsonData["perk0"]
        self.perk3 = jsonData["perk3"]
        self.perk2 = jsonData["perk2"]
        self.perk5 = jsonData["perk5"]
        self.perk4 = jsonData["perk4"]
        self.perk3Var1 = jsonData["perk3Var1"]
        self.damageSelfMitigated = jsonData["damageSelfMitigated"]
        self.magicalDamageTaken = jsonData["magicalDamageTaken"]
        self.firstInhibitorKill = jsonData["firstInhibitorKill"]
        self.trueDamageTaken = jsonData["trueDamageTaken"]
        #self.nodeNeutralize = jsonData["nodeNeutralize"]
        self.assists = jsonData["assists"]
        self.combatPlayerScore = jsonData["combatPlayerScore"]
        self.perkPrimaryStyle = jsonData["perkPrimaryStyle"]
        self.goldSpent = jsonData["goldSpent"]
        self.trueDamageDealt = jsonData["trueDamageDealt"]
        self.participantId = jsonData["participantId"]
        self.totalDamageTaken = jsonData["totalDamageTaken"]
        self.physicalDamageDealt = jsonData["physicalDamageDealt"]
        self.sightWardsBoughtInGame = jsonData["sightWardsBoughtInGame"]
        self.totalDamageDealtToChampions = jsonData["totalDamageDealtToChampions"]
        self.physicalDamageTaken = jsonData["physicalDamageTaken"]
        self.totalPlayerScore = jsonData["totalPlayerScore"]
        self.win = jsonData["win"]
        self.objectivePlayerScore = jsonData["objectivePlayerScore"]
        self.totalDamageDealt = jsonData["totalDamageDealt"]
        self.item1 = jsonData["item1"]
        self.neutralMinionsKilledEnemyJungle = jsonData["neutralMinionsKilledEnemyJungle"]
        self.deaths = jsonData["deaths"]
        self.wardsPlaced = jsonData["wardsPlaced"]
        self.perkSubStyle = jsonData["perkSubStyle"]
        self.turretKills = jsonData["turretKills"]
        self.firstBloodKill = jsonData["firstBloodKill"]
        self.trueDamageDealtToChampions = jsonData["trueDamageDealtToChampions"]
        self.goldEarned = jsonData["goldEarned"]
        self.killingSprees = jsonData["killingSprees"]
        self.unrealKills = jsonData["unrealKills"]
        #self.altarsCaptured = jsonData["altarsCaptured"]
        self.firstTowerAssist = jsonData["firstTowerAssist"]
        self.firstTowerKill = jsonData["firstTowerKill"]
        self.champLevel = jsonData["champLevel"]
        self.doubleKills = jsonData["doubleKills"]
        #self.nodeCaptureAssist = jsonData["nodeCaptureAssist"]
        self.inhibitorKills = jsonData["inhibitorKills"]
        self.firstInhibitorAssist = jsonData["firstInhibitorAssist"]
        self.perk0Var1 = jsonData["perk0Var1"]
        self.perk0Var2 = jsonData["perk0Var2"]
        self.perk0Var3 = jsonData["perk0Var3"]
        self.visionWardsBoughtInGame = jsonData["visionWardsBoughtInGame"]
        #self.altarsNeutralized = jsonData["altarsNeutralized"]
        self.pentaKills = jsonData["pentaKills"]
        self.totalHeal = jsonData["totalHeal"]	
        self.totalMinionsKilled = jsonData["totalMinionsKilled"]
        self.timeCCingOthers = jsonData["timeCCingOthers"]
        return

class RuneDto:
    def __init__(self, jsonData):
        self.jsonData = jsonData
        self.runeId = jsonData["runeId"]
        self.rank = jsonData["rank"]
        return

class ParticipantTimelineDto:
    def __init__(self, jsonData):
        self.jsonData = jsonData
        self.lane = jsonData["lane"]
        self.participantId = jsonData["participantId"]
        self.csDiffPerMinDeltas = jsonData["csDiffPerMinDeltas"]
        self.goldPerMinDeltas = jsonData["goldPerMinDeltas"]
        self.xpDiffPerMinDeltas = jsonData["xpDiffPerMinDeltas"]
        self.creepsPerMinDeltas = jsonData["creepsPerMinDeltas"]
        self.xpPerMinDeltas = jsonData["xpPerMinDeltas"]
        self.role = jsonData["role"]
        self.damageTakenDiffPerMinDeltas = jsonData["damageTakenDiffPerMinDeltas"]
        self.damageTakenPerMinDeltas = jsonData["damageTakenPerMinDeltas"]
        return

class MasteryDto:
    def __init__(self, jsonData):
        self.jsonData = jsonData
        self.masteryId = jsonData["masteryId"]
        self.rank = jsonData["rank"]
        return