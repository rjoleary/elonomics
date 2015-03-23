from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from elonomics.models import Player, Match, Outcome


def players(request):
    players = Player.objects.order_by('full_name')
    context = {'players': players}
    return render(request, 'elonomics/players.html', context)


def player(request, user_name):
    player = get_object_or_404(Player, user_name=user_name)
    games = (player.player1.all() | player.player2.all()).order_by('-time_played')
    context = {'player': player, 'games': games}
    return render(request, 'elonomics/player.html', context)


def games(request):
    games = Match.objects.order_by('-time_played')
    players = Player.objects.order_by('full_name')
    outcomes = Outcome.objects.all()
    context = {'games': games, 'players': players, 'outcomes': outcomes}
    return render(request, 'elonomics/games.html', context)


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
    o = Outcome.objects.get(verb=request.POST['outcome'])
    m = Match(
            time_played=request.POST['time_played'],
            story=request.POST['story'],
            player1=p1,
            player2=p2,
            player1_before_game_elo=p1.elo_score,
            player2_before_game_elo=p2.elo_score,
            outcome=o
    )
    m.save()
    return HttpResponseRedirect(reverse('games'))


def support(request):
    return render(request, 'elonomics/support.html')
