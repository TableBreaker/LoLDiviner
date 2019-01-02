#coding = utf-8
import json

class MatchDto:
    def __init__(self, jsonData):
        #self.jsonData = jsonData
        # self.seasonId = jsonData["seasonId"] if "seasonId" in jsonData else None
        self.queueId = jsonData["queueId"] if "queueId" in jsonData else None
        self.gameId = jsonData["gameId"] if "gameId" in jsonData else None
        self.participantIdentities = []
        if "participantIdentities" in jsonData:
            for item in jsonData["participantIdentities"]:
                self.participantIdentities.append(ParticipantIdentityDto(item))
        # self.gameVersion = jsonData["gameVersion"] if "gameVersion" in jsonData else None
        # self.platformId = jsonData["platformId"] if "platformId" in jsonData else None
        # self.gameMode = jsonData["gameMode"] if "gameMode" in jsonData else None
        # self.mapId = jsonData["mapId"] if "mapId" in jsonData else None
        # self.gameType = jsonData["gameType"] if "gameType" in jsonData else None
        self.teams = []
        if "teams" in jsonData:
            for item in jsonData["teams"]:
                self.teams.append(TeamStatsDto(item))
        self.participants = []
        if "participants" in jsonData:
            for item in jsonData["participants"]:
                self.participants.append(ParticipantDto(item))
        self.gameDuration = jsonData["gameDuration"] if "gameDuration" in jsonData else None
        self.gameCreation = jsonData["gameCreation"] if "gameCreation" in jsonData else None

    def processMatchData(self, targetAccountId):
        participantId = 0
        for i, v in enumerate(self.participantIdentities):
            if v.player.accountId != targetAccountId:
                self.participantIdentities[i] = None
            else:
                participantId = v.participantId
        
        for i, v in enumerate(self.participants):
            if v.participantId != participantId:
                self.participants[i] = None
        
class ParticipantIdentityDto:
    def __init__(self, jsonData):
        #self.jsonData = jsonData
        self.player = PlayerDto(jsonData["player"]) if "player" in jsonData else None
        self.participantId = jsonData["participantId"] if "participantId" in jsonData else None
        return

class PlayerDto:
    def __init__(self, jsonData):
        #self.jsonData = jsonData
        # self.currentPlatformId = jsonData["currentPlatformId"] if "currentPlatformId" in jsonData else None
        self.summonerName = jsonData["summonerName"] if "summonerName" in jsonData else None
        # self.matchHistoryUri = jsonData["matchHistoryUri"] if "matchHistoryUri" in jsonData else None
        # self.platformId = jsonData["platformId"] if "platformId" in jsonData else None
        self.currentAccountId = jsonData["currentAccountId"] if "currentAccountId" in jsonData else None
        # self.profileIcon = jsonData["profileIcon"] if "profileIcon" in jsonData else None
        self.summonerId = jsonData["summonerId"] if "summonerId" in jsonData else None
        self.accountId = jsonData["accountId"] if "accountId" in jsonData else None
        return

class TeamStatsDto:
    def __init__(self, jsonData):
        #self.jsonData = jsonData
        self.firstDragon = jsonData["firstDragon"] if "firstDragon" in jsonData else None
        self.firstInhibitor = jsonData["firstInhibitor"] if "firstInhibitor" in jsonData else None
        self.bans = []
        if "bans" in jsonData:
            for item in jsonData["bans"]:
                self.bans.append(TeamBansDto(item))
        self.baronKills = jsonData["baronKills"] if "baronKills" in jsonData else None
        self.firstRiftHerald = jsonData["firstRiftHerald"] if "firstRiftHerald" in jsonData else None
        self.firstBaron = jsonData["firstBaron"] if "firstBaron" in jsonData else None
        self.riftHeraldKills = jsonData["riftHeraldKills"] if "riftHeraldKills" in jsonData else None
        self.firstBlood = jsonData["firstBlood"] if "firstBlood" in jsonData else None
        self.teamId = jsonData["teamId"] if "teamId" in jsonData else None
        self.firstTower = jsonData["firstTower"] if "firstTower" in jsonData else None
        self.vilemawKills = jsonData["vilemawKills"] if "vilemawKills" in jsonData else None
        self.inhibitorKills = jsonData["inhibitorKills"] if "inhibitorKills" in jsonData else None
        self.towerKills = jsonData["towerKills"] if "towerKills" in jsonData else None
        self.dominionVictoryScore = jsonData["dominionVictoryScore"] if "dominionVictoryScore" in jsonData else None
        self.win = jsonData["win"] if "win" in jsonData else None
        self.dragonKills = jsonData["dragonKills"] if "dragonKills" in jsonData else None
        return

class TeamBansDto:
    def __init__(self, jsonData):
        #self.jsonData = jsonData
        self.pickTurn = jsonData["pickTurn"] if "pickTurn" in jsonData else None
        self.championId = jsonData["championId"] if "championId" in jsonData else None
        return

class ParticipantDto:
    def __init__(self, jsonData):
        #self.jsonData = jsonData
        self.stats = ParticipantStatsDto(jsonData["stats"]) if "stats" in jsonData else None
        self.participantId = jsonData["participantId"] if "stats" in jsonData else None
        self.runes = []
        if "runes" in jsonData:
            for item in jsonData["runes"]:
                self.runes.append(RuneDto(item))
        self.timeline = ParticipantTimelineDto(jsonData["timeline"]) if "timeline" in jsonData else None
        self.teamId = jsonData["teamId"] if "teamId" in jsonData else None
        self.spell2Id = jsonData["spell2Id"] if "spell2Id" in jsonData else None
        self.masteries = []
        if "masteries" in jsonData:
            for item in jsonData["masteries"]:
                self.masteries.append(MasteryDto(item))
        self.highestAchievedSeasonTier = jsonData["highestAchievedSeasonTier"] if "highestAchievedSeasonTier" in jsonData else None
        self.spell1Id = jsonData["spell1Id"] if "spell1Id" in jsonData else None
        self.championId = jsonData["championId"] if "championId" in jsonData else None
        return

class ParticipantStatsDto:
    def __init__(self, jsonData):
        #self.jsonData = jsonData
        self.firstBloodAssist = jsonData["firstBloodAssist"] if "firstBloodAssist" in jsonData else None
        self.visionScore = jsonData["visionScore"] if "visionScore" in jsonData else None
        self.magicDamageDealtToChampions = jsonData["magicDamageDealtToChampions"] if "magicDamageDealtToChampions" in jsonData else None
        self.damageDealtToObjectives = jsonData["damageDealtToObjectives"] if "damageDealtToObjectives" in jsonData else None	
        self.totalTimeCrowdControlDealt = jsonData["totalTimeCrowdControlDealt"] if "totalTimeCrowdControlDealt" in jsonData else None
        self.longestTimeSpentLiving = jsonData["longestTimeSpentLiving"] if "longestTimeSpentLiving" in jsonData else None
        # self.perk1Var1 = jsonData["perk1Var1"] if "perk1Var1" in jsonData else None
        # self.perk1Var3 = jsonData["perk1Var3"] if "perk1Var3" in jsonData else None
        # self.perk1Var2 = jsonData["perk1Var2"] if "perk1Var2" in jsonData else None
        self.tripleKills = jsonData["perk1Var2"] if "perk1Var2" in jsonData else None
        # self.perk3Var3 = jsonData["perk3Var3"] if "perk3Var3" in jsonData else None
        self.nodeNeutralizeAssist = jsonData["nodeNeutralizeAssist"] if "nodeNeutralizeAssist" in jsonData else None
        # self.perk3Var2 = jsonData["perk3Var2"] if "perk3Var2" in jsonData else None
        # self.playerScore9 = jsonData["playerScore9"] if "playerScore9" in jsonData else None
        # self.playerScore8 = jsonData["playerScore8"] if "playerScore8" in jsonData else None
        self.kills = jsonData["kills"] if "kills" in jsonData else None
        # self.playerScore1 = jsonData["playerScore1"] if "playerScore1" in jsonData else None
        # self.playerScore0 = jsonData["playerScore0"] if "playerScore0" in jsonData else None
        # self.playerScore3 = jsonData["playerScore3"] if "playerScore3" in jsonData else None
        # self.playerScore2 = jsonData["playerScore2"] if "playerScore2" in jsonData else None
        # self.playerScore5 = jsonData["playerScore5"] if "playerScore5" in jsonData else None
        # self.playerScore4 = jsonData["playerScore4"] if "playerScore4" in jsonData else None
        # self.playerScore7 = jsonData["playerScore7"] if "playerScore7" in jsonData else None
        # self.playerScore6 = jsonData["playerScore6"] if "playerScore6" in jsonData else None
        # self.perk5Var1 = jsonData["perk5Var1"] if "perk5Var1" in jsonData else None
        # self.perk5Var3 = jsonData["perk5Var3"] if "perk5Var3" in jsonData else None
        # self.perk5Var2 = jsonData["perk5Var2"] if "perk5Var2" in jsonData else None
        self.totalScoreRank = jsonData["totalScoreRank"] if "totalScoreRank" in jsonData else None
        self.neutralMinionsKilled = jsonData["neutralMinionsKilled"] if "neutralMinionsKilled" in jsonData else None
        self.damageDealtToTurrets = jsonData["damageDealtToTurrets"] if "damageDealtToTurrets" in jsonData else None
        self.physicalDamageDealtToChampions = jsonData["physicalDamageDealtToChampions"] if "physicalDamageDealtToChampions" in jsonData else None
        self.nodeCapture = jsonData["nodeCapture"] if "nodeCapture" in jsonData else None
        self.largestMultiKill = jsonData["largestMultiKill"] if "largestMultiKill" in jsonData else None
        # self.perk2Var2 = jsonData["perk2Var2"] if "perk2Var2" in jsonData else None
        # self.perk2Var3 = jsonData["perk2Var3"] if "perk2Var3" in jsonData else None
        self.totalUnitsHealed = jsonData["totalUnitsHealed"] if "totalUnitsHealed" in jsonData else None
        # self.perk2Var1 = jsonData["perk2Var1"] if "perk2Var1" in jsonData else None
        # self.perk4Var1 = jsonData["perk4Var1"] if "perk4Var1" in jsonData else None
        # self.perk4Var2 = jsonData["perk4Var2"] if "perk4Var2" in jsonData else None
        # self.perk4Var3 = jsonData["perk4Var3"] if "perk4Var3" in jsonData else None
        self.wardsKilled = jsonData["wardsKilled"] if "wardsKilled" in jsonData else None
        self.largestCriticalStrike = jsonData["largestCriticalStrike"] if "largestCriticalStrike" in jsonData else None
        self.largestKillingSpree = jsonData["largestKillingSpree"] if "largestKillingSpree" in jsonData else None
        self.quadraKills = jsonData["quadraKills"] if "quadraKills" in jsonData else None
        self.teamObjective = jsonData["teamObjective"] if "teamObjective" in jsonData else None
        self.magicDamageDealt = jsonData["magicDamageDealt"] if "magicDamageDealt" in jsonData else None
        self.item2 = jsonData["item2"] if "item2" in jsonData else None
        self.item3 = jsonData["item3"] if "item3" in jsonData else None
        self.item0 = jsonData["item0"] if "item0" in jsonData else None
        self.neutralMinionsKilledTeamJungle = jsonData["neutralMinionsKilledTeamJungle"] if "neutralMinionsKilledTeamJungle" in jsonData else None
        self.item6 = jsonData["item6"] if "item6" in jsonData else None
        self.item4 = jsonData["item4"] if "item4" in jsonData else None
        self.item5 = jsonData["item5"] if "item5" in jsonData else None
        self.perk1 = jsonData["perk1"] if "perk1" in jsonData else None
        self.perk0 = jsonData["perk0"] if "perk0" in jsonData else None
        self.perk3 = jsonData["perk3"] if "perk3" in jsonData else None
        self.perk2 = jsonData["perk2"] if "perk2" in jsonData else None
        self.perk5 = jsonData["perk5"] if "perk5" in jsonData else None
        self.perk4 = jsonData["perk4"] if "perk4" in jsonData else None
        self.damageSelfMitigated = jsonData["damageSelfMitigated"] if "damageSelfMitigated" in jsonData else None
        self.magicalDamageTaken = jsonData["magicalDamageTaken"] if "magicalDamageTaken" in jsonData else None
        self.firstInhibitorKill = jsonData["firstInhibitorKill"] if "firstInhibitorKill" in jsonData else None
        self.trueDamageTaken = jsonData["trueDamageTaken"] if "trueDamageTaken" in jsonData else None
        self.nodeNeutralize = jsonData["nodeNeutralize"] if "nodeNeutralize" in jsonData else None
        self.assists = jsonData["assists"] if "assists" in jsonData else None
        self.combatPlayerScore = jsonData["combatPlayerScore"] if "combatPlayerScore" in jsonData else None
        self.perkPrimaryStyle = jsonData["perkPrimaryStyle"] if "perkPrimaryStyle" in jsonData else None
        self.goldSpent = jsonData["goldSpent"] if "goldSpent" in jsonData else None
        self.trueDamageDealt = jsonData["trueDamageDealt"] if "trueDamageDealt" in jsonData else None
        self.participantId = jsonData["participantId"] if "participantId" in jsonData else None
        self.totalDamageTaken = jsonData["totalDamageTaken"] if "totalDamageTaken" in jsonData else None
        self.physicalDamageDealt = jsonData["physicalDamageDealt"] if "physicalDamageDealt" in jsonData else None
        self.sightWardsBoughtInGame = jsonData["sightWardsBoughtInGame"] if "sightWardsBoughtInGame" in jsonData else None
        self.totalDamageDealtToChampions = jsonData["totalDamageDealtToChampions"] if "totalDamageDealtToChampions" in jsonData else None
        self.physicalDamageTaken = jsonData["physicalDamageTaken"] if "physicalDamageTaken" in jsonData else None
        self.totalPlayerScore = jsonData["totalPlayerScore"] if "totalPlayerScore" in jsonData else None
        self.win = jsonData["win"] if "win" in jsonData else None
        self.objectivePlayerScore = jsonData["objectivePlayerScore"] if "objectivePlayerScore" in jsonData else None
        self.totalDamageDealt = jsonData["totalDamageDealt"] if "totalDamageDealt" in jsonData else None
        self.item1 = jsonData["item1"] if "item1" in jsonData else None
        self.neutralMinionsKilledEnemyJungle = jsonData["neutralMinionsKilledEnemyJungle"] if "neutralMinionsKilledEnemyJungle" in jsonData else None
        self.deaths = jsonData["deaths"] if "deaths" in jsonData else None
        self.wardsPlaced = jsonData["wardsPlaced"] if "wardsPlaced" in jsonData else None
        self.perkSubStyle = jsonData["perkSubStyle"] if "perkSubStyle" in jsonData else None
        self.turretKills = jsonData["turretKills"] if "turretKills" in jsonData else None
        self.firstBloodKill = jsonData["firstBloodKill"] if "firstBloodKill" in jsonData else None
        self.trueDamageDealtToChampions = jsonData["trueDamageDealtToChampions"] if "trueDamageDealtToChampions" in jsonData else None
        self.goldEarned = jsonData["goldEarned"] if "goldEarned" in jsonData else None
        self.killingSprees = jsonData["killingSprees"] if "killingSprees" in jsonData else None
        self.unrealKills = jsonData["unrealKills"] if "unrealKills" in jsonData else None
        self.altarsCaptured = jsonData["altarsCaptured"] if "altarsCaptured" in jsonData else None
        self.firstTowerAssist = jsonData["firstTowerAssist"] if "firstTowerAssist" in jsonData else None
        self.firstTowerKill = jsonData["firstTowerKill"] if "firstTowerKill" in jsonData else None
        self.champLevel = jsonData["champLevel"] if "champLevel" in jsonData else None
        self.doubleKills = jsonData["doubleKills"] if "doubleKills" in jsonData else None
        self.nodeCaptureAssist = jsonData["nodeCaptureAssist"] if "nodeCaptureAssist" in jsonData else None
        self.inhibitorKills = jsonData["inhibitorKills"] if "inhibitorKills" in jsonData else None
        self.firstInhibitorAssist = jsonData["firstInhibitorAssist"] if "firstInhibitorAssist" in jsonData else None
        # self.perk0Var1 = jsonData["perk0Var1"] if "perk0Var1" in jsonData else None
        # self.perk0Var2 = jsonData["perk0Var2"] if "perk0Var2" in jsonData else None
        # self.perk0Var3 = jsonData["perk0Var3"] if "perk0Var3" in jsonData else None
        self.visionWardsBoughtInGame = jsonData["visionWardsBoughtInGame"] if "visionWardsBoughtInGame" in jsonData else None
        self.altarsNeutralized = jsonData["altarsNeutralized"] if "altarsNeutralized" in jsonData else None
        self.pentaKills = jsonData["pentaKills"] if "pentaKills" in jsonData else None
        self.totalHeal = jsonData["totalHeal"] if "totalHeal" in jsonData else None
        self.totalMinionsKilled = jsonData["totalMinionsKilled"] if "totalMinionsKilled" in jsonData else None
        self.timeCCingOthers = jsonData["timeCCingOthers"] if "timeCCingOthers" in jsonData else None
        return
    
class RuneDto:
    def __init__(self, jsonData):
        #self.jsonData = jsonData
        self.runeId = jsonData["runeId"] if "runeId" in jsonData else None
        self.rank = jsonData["rank"] if "rank" in jsonData else None
        return

class ParticipantTimelineDto:
    def __init__(self, jsonData):
        #self.jsonData = jsonData
        self.lane = jsonData["lane"]
        self.participantId = jsonData["participantId"] if "participantId" in jsonData else None
        self.csDiffPerMinDeltas = jsonData["csDiffPerMinDeltas"] if "csDiffPerMinDeltas" in jsonData else None
        self.goldPerMinDeltas = jsonData["goldPerMinDeltas"] if "goldPerMinDeltas" in jsonData else None
        self.xpDiffPerMinDeltas = jsonData["xpDiffPerMinDeltas"] if "xpDiffPerMinDeltas" in jsonData else None
        self.creepsPerMinDeltas = jsonData["creepsPerMinDeltas"] if "creepsPerMinDeltas" in jsonData else None
        self.xpPerMinDeltas = jsonData["xpPerMinDeltas"] if "xpPerMinDeltas" in jsonData else None
        self.role = jsonData["role"] if "role" in jsonData else None
        self.damageTakenDiffPerMinDeltas = jsonData["damageTakenDiffPerMinDeltas"] if "damageTakenDiffPerMinDeltas" in jsonData else None
        self.damageTakenPerMinDeltas = jsonData["damageTakenPerMinDeltas"] if "damageTakenPerMinDeltas" in jsonData else None
        return

class MasteryDto:
    def __init__(self, jsonData):
        #self.jsonData = jsonData
        self.masteryId = jsonData["masteryId"] if "masteryId" in jsonData else None
        self.rank = jsonData["rank"] if "rank" in jsonData else None
        return