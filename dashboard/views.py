from django.shortcuts import render
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.static import players
from .models import Player


def get_player_by_name(player_name: str):
    # grab all players
    all_players = players.get_players()
    # for every player available search for the
    # player matching the name we provided
    found_player = [player for player in all_players
                    if player['full_name'] == player_name][0]
    # grab player id for future usuage
    player_id = found_player['id']
    return player_id


def get_nba_player_info(player_id):
    # grab all common player info based on provided player_id
    player_info = commonplayerinfo.CommonPlayerInfo(player_id)
    player_data = player_info.get_normalized_dict()['CommonPlayerInfo'][0]
    return player_data


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


def search(request):
    # defines what happens when there is a POST req
    if request.method == "POST":
        title = request.POST.get("q")
        return render(request, 'search_results.html', {'title': title})
    # defines what happens when there is a GET req
    else:
        return render(request, 'searchbar.html')
