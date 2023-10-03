from etl.extract_data import get_champions_league_teams

def test_get_champions_league_teams():
    champions_league_clubs = get_champions_league_teams()
    assert len(champions_league_clubs) == 32
    assert type(champions_league_clubs[0]) == type(dict())
    assert type(champions_league_clubs[15]) == type({})
    assert type(champions_league_clubs[31]) == type({})