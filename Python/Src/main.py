#coding=utf-8
import requests
import json

def requestSummonerData(summonerName, APIKey):

    URL = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    print (URL)
    response = requests.get(URL)
    return response.json()

def requestRankedData(ID, APIKey):
    URL= "https://na1.api.riotgames.com/lol/league/v3/positions/by-summoner/"+ID+"?api_key="+APIKey
    print (URL)
    response = requests.get(URL)
    return response.json()


def main():

    summonerName = (str)(input('Type your Summoner Name here: '))
    APIKey = (str)(input('Copy and paste your API Key here: '))
    responseJSON  = requestSummonerData(summonerName, APIKey)

    print(responseJSON)
    ID = responseJSON ['id']
    ID = str(ID)
    print (ID)
    responseJSON2 = requestRankedData(ID, APIKey)
    print (responseJSON2[ID][0]['tier'])
    print (responseJSON2[ID][0]['entries'][0]['rank'])
    print (responseJSON2[ID][0]['entries'][0]['leaguePoints'])

def requestMasterQueue():
    return None

def requestChallengerQueue():
    return None

def requestMatchData(summonerName, matchId, APIKey):
    return None


if __name__ == "__main__":
    main()