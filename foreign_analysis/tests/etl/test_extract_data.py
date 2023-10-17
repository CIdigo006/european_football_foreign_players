from etl.extract_data import get_league_clubs

def test_get_league_clubs():
    champions_league_clubs = get_league_clubs()
    
    assert len(champions_league_clubs) == 32
    assert type(champions_league_clubs[0]) == type(dict())
    assert type(champions_league_clubs[15]) == type({})
    assert type(champions_league_clubs[31]) == type({})