from collections import defaultdict
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from elonomics.models import Player, Game


def players(request):
    players = Player.objects.order_by('full_name')
    return render(request, 'elonomics/players.html', {'players': players})


def player(request, user_name):
    player = get_object_or_404(Player, user_name=user_name)
    games = (player.player1.all() | player.player2.all()).order_by('-time_played')
    return render(request, 'elonomics/player.html', {
        'player': player,
        'games': games
    })


def games(request):
    games = Game.objects.order_by('-time_played')
    # Split games into groups based on day.
    game_groups = defaultdict(list)
    for game in games:
        game_groups['{0:%A, %B} {0.day}'.format(game.time_played)].append(game)
    players = Player.objects.order_by('full_name')
    outcomes = Game.OUTCOME_CHOICES
    return render(request, 'elonomics/games.html', {
        'game_groups': dict(game_groups),
        'players': players,
        'outcomes': outcomes
    })


def submit_game(request):
    try:
        # TODO: catch KeyError
        p1 = Player.objects.get(user_name=request.POST['player1'])
        p2 = Player.objects.get(user_name=request.POST['player2'])
    except (Player.DoesNotExist):
        return render(request, 'elonomics/games.html', {
            'error_message': "Player name does not exist."
        })

    # TODO: sign-offs
    # TODO: update score
    m = Game(
            time_played=request.POST['time_played'],
            story=request.POST['story'],
            player1=p1,
            player2=p2,
            player1_before_game_elo=p1.elo_score,
            player2_before_game_elo=p2.elo_score,
            outcome=request.POST['outcome']
    )
    m.save()
    return HttpResponseRedirect(reverse('games'))
