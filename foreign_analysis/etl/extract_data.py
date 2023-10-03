import requests
import time
import pandas as pd
from settings import api_key, api_host, api_domain
api_headers = {
        	"X-RapidAPI-Key": api_key,
        	"X-RapidAPI-Host": api_host
        }


# The purpose of this portion here is to get all the teams that are in the champions league. Then from there we will look at all
# the leagues that sent a team to the champions league(we are starting from here as it's Europe's most premiere competition)
# while looking at how the teams in the champions league are  displayed we see they are displayed in a dictionary of a list of 
# dictionaries with each dictionary being a team and containing the following key value pairs ("id": "teamid",  
# "name": "team_name", "image": "link_to_team_image")
def get_champions_league_clubs():

    url = "https://transfermarket.p.rapidapi.com/clubs/list-by-competition"
    querystring = {"id":"cl","domain":api_domain}
    headers = api_headers
    response = requests.get(url, headers=headers, params=querystring)
    clubs_json = response.json()["clubs"]

    return clubs_json

# Using the data retrieved from get_champions_league_teams or another function that gets a list of clubs. We will call 
# some information about each team in the list and get the domestic leagues that teams in the list belong to
def get_leagues_from_clubs(clubs):

    clubs = clubs

    # loop through the list of dictionary of clubs. With each loop hit the api to get the domestic league each team in the
    # the league belongs to and add them to the 'clubs' dictionary as "league": "league identifier" then from there add the
    # league to a seperate list we'll call leagues and apply a set to that list to get all the leagues involved in the
    # competition without any duplicates or repeats
    clubs_leagues = []
    n = 0

    for club in clubs:
        url = "https://transfermarket.p.rapidapi.com/clubs/get-header-info"

        querystring = {"id":club["id"],"domain":api_domain}

        headers = api_headers

        response = requests.get(url, headers=headers, params=querystring)
    
        # breakpoint()
        time.sleep(1)
        clubs_leagues.append(response.json()["club"]["leagueID"])
        clubs[n].update({"leagueID": response.json()["club"]["leagueID"], "leagueName": response.json()["club"]["leagueName"]})
        n += 1
        
    clubs_leagues_cleaned = list(set(clubs_leagues))
    breakpoint()
    return clubs_leagues_cleaned