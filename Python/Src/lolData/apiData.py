#coding=utf-8

APIKEY = "RGAPI-939b3ebe-3a4c-4fdc-8b7d-202d41d82459"

class ApiUrl:
    MASTER_LEAGUE_API = "/lol/league/v4/masterleagues/by-queue/"
    GRANDMASTER_LEAGUE_API = "/lol/league/v4/grandmasterleagues/by-queue/"
    CHALLENGER_LEAGUE_API = "/lol/league/v4/challengerleagues/by-queue/"
    MATCH_API = "/lol/match/v4/matches/"
    ACCOUNT_MATCH_LIST_API = "/lol/match/v4/matchlists/by-account/"
    SUMMONER_DATA_API = "/lol/summoner/v4/summoners/by-name/"

class ApiParam:
    SOLORANK = "RANKED_SOLO_5x5"
    FLEXSR = "RANKED_FLEX_SR"
    FLEXTT = "RANKED_FLEX_TT"