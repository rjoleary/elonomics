from django.shortcuts import render
from elonomics.models import Player, Match


def scoreboard(request):
    SCOREBOARD_SIZE = 10
    top_players = Player.objects.order_by('-elo_score')[:SCOREBOARD_SIZE]
    context = {'top_players': top_players}
    return render(request, 'elonomics/scoreboard.html', context)


def history(request):
    matches = Match.objects.order_by('-time_played')
    context = {'matches': matches}
    return render(request, 'elonomics/history.html', context)


def players(request):
    players = Player.objects.order_by('full_name')
    context = {'players': players}
    return render(request, 'elonomics/players.html', context)


def player(request, user_name):
    try:
        player = Player.objects.get(user_name=user_name)
    except Player.DoesNotExist:
        raise Http404("Player does not exist!")
    matches = (player.player1.all() | player.player2.all()).order_by('-time_played')
    context = {'player': player, 'matches': matches}
    return render(request, 'elonomics/player.html', context)


def support(request):
    return render(request, 'elonomics/support.html')
