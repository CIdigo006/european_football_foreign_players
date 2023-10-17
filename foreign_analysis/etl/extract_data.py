import requests
import time
import pandas as pd
from settings import api_key, api_host, api_domain
api_headers = {
        	"X-RapidAPI-Key": api_key,
        	"X-RapidAPI-Host": api_host
        }


# The purpose of this portion here is to get all the teams that are in the league. Then from there we will look at all
# the clubs in that league while looking at how the teams in the league are displayed we see they are displayed in a
# dictionary of a list of dictionaries with each dictionary being a team and containing the following 
# key value pairs ("id": "teamid", "name": "team_name", "image": "link_to_team_image")
def get_league_clubs():

    # league_id = str(input("Enter the league_id of the league to explore: "))
    url = "https://transfermarket.p.rapidapi.com/clubs/list-by-competition"
    querystring = {"id": "cl","domain":api_domain}
    headers = api_headers
    response = requests.get(url, headers=headers, params=querystring)
    league_clubs_json = response.json()["clubs"]
    # breakpoint()
    return league_clubs_json


# Using the data retrieved from get_champions_league_teams or another function that gets a list of clubs. We will call 
# some information about each team in the list and get the domestic leagues that teams in the list belong to
# along with an updated version of our original list with their domestic leagues now included    
def get_leagues_from_clubs():

    clubs_json = get_league_clubs()

    # loop through the list of dictionary of clubs. With each loop hit the api to get the domestic league each team in the
    # list belongs to and add them to the 'clubs_json' list of dictionaries as "league": "league identifier" then from there add 
    # the league to a seperate list we'll call clubs_leagues and apply a set to that list to get all the leagues involved in the
    # competition without any duplicates or repeats and call the cleaned one clubs_leagues_cleaned
    clubs_leagues_info = {}
    clubs_leagues = []
    n = 0
    # breakpoint()

    for club in clubs_json:
        url = "https://transfermarket.p.rapidapi.com/clubs/get-header-info"
        # breakpoint()

        querystring = {"id":club["id"],"domain":api_domain}

        headers = api_headers

        response = requests.get(url, headers=headers, params=querystring)
    
        # breakpoint()
        time.sleep(1)
        clubs_json[n].update({"leagueID": response.json()["club"]["leagueID"], "leagueName": response.json()["club"]["leagueName"]})
        if not clubs_leagues_info:
            clubs_leagues_info[response.json()["club"]["leagueID"]] = response.json()["club"]["leagueName"]
            clubs_leagues.append(response.json()["club"]["leagueID"])
        elif response.json()["club"]["leagueID"] not in clubs_leagues:
            clubs_leagues_info[response.json()["club"]["leagueID"]] = response.json()["club"]["leagueName"]
            clubs_leagues.append(response.json()["club"]["leagueID"])
        n += 1
        
    # breakpoint()
    return (clubs_json, clubs_leagues_info)


# The purpose of this function is to get the clubs that are located in all the different leagues that are passed in to 
# it. So if 5 separate leagues are fed into it, it'll produce all the teams for those 5 leagues
def get_clubs_leagues():
    
    leagues_from_clubs = get_leagues_from_clubs()
    # breakpoint()
    league_ids = list(leagues_from_clubs[1].keys())
    leagues_info = []
    # breakpoint()
    for league_id in league_ids:
        # breakpoint()
        url = "https://transfermarket.p.rapidapi.com/clubs/list-by-competition"
        querystring = {"id": league_id,"domain":api_domain}
        headers = api_headers
        response = requests.get(url, headers=headers, params=querystring)
        league_clubs_json = response.json()["clubs"]
        leagues_info.append({"leauge_id":league_id, "league_name": leagues_from_clubs[1][league_id], 
                             "league_clubs":league_clubs_json})    

    # breakpoint()
    return