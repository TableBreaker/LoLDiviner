#coding=utf-8

APIKEY = "RGAPI-6d7c4811-9073-4899-ab14-3a798d3d6f13"

class ApiUrl:
    MASTER_LEAGUE_API = "/lol/league/v4/masterleagues/by-queue/"
    GRANDMASTER_LEAGUE_API = "/lol/league/v4/grandmasterleagues/by-queue/"
    CHALLENGER_LEAGUE_API = "/lol/league/v4/challengerleagues/by-queue/"
    MATCH_API = "/lol/match/v4/matches/"
    ACCOUNT_MATCH_LIST_API = "/lol/match/v4/matchlists/by-account/"
    SUMMONER_DATA_API = "/lol/summoner/v4/summoners/by-name/"
    SUMMONER_DATA_BY_ACCOUNT_API = "/lol/summoner/v4/summoners/by-account/"

class ApiParam:
    SOLORANK = "RANKED_SOLO_5x5"
    FLEXSR = "RANKED_FLEX_SR"
    FLEXTT = "RANKED_FLEX_TT"