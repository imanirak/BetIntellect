from django.shortcuts import render
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players
from .models import Player


def get_all_players():
    all_players = players.get_players()
    name = input() 
    [player for player in all_players if player['full_name'] == name][0]
    player_id = f"{name} is player"
    return player_id


def get_nba_player_info(player_id):
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
    return player_info.get_normalized_dict()['CommonPlayerInfo'][0]


def dashboard(request):
    # Fetch NBA player data using the nba_api package
    player_id = 203999  # Replace with the actual player ID
    player_data = get_nba_player_info(player_id)

    # Create or update Player object in the database
    player, created = Player.objects.get_or_create(
        nba_id=player_data['PERSON_ID'],
        defaults={
            'full_name': player_data['DISPLAY_FIRST_LAST'],
            'position': player_data['POSITION'],
        }
    )

    context = {
        'player': player,
    }

    return render(request, 'dashboard.html', context)


#grab all players from specific teams
#filter through them all
#list top players