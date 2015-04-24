from collections import OrderedDict
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from elonomics.models import Player, Game
import re


def games(request):
    games = Game.objects.order_by('-time_played')
    # Split games into groups based on day.
    game_groups = OrderedDict()
    for game in games:
        key = '{0:%A, %B} {0.day}, {0.year}'.format(game.time_played)
        if key in game_groups:
            game_groups[key].insert(0, game)
        else:
            game_groups[key] = [game]

    players = Player.objects.order_by('full_name')
    outcomes = Game.OUTCOME_CHOICES
    return render(request, 'elonomics/games.html', {
        'game_groups': game_groups,
        'players': players,
        'outcomes': outcomes
    })


def submit_game(request):
    try:
        t = request.POST['time_played'].strip()
        s = request.POST['story'].strip()
        p1 = request.POST['player1']
        p2 = request.POST['player2']
        s1 = request.POST['signoff1']
        s2 = request.POST['signoff2']
        o = int(request.POST['outcome'])
    except KeyError:
        messages.add_message(request, messages.ERROR, "Invalid form submit. Please try again.")
        return HttpResponseRedirect(reverse('games'))

    if not re.match('^\d\d\d\d-\d\d-\d\d \d\d:\d\d$', t):
        messages.add_message(request, messages.ERROR, "I am truly sorry for the lack of calendar. Please input the time in the format YYYY-MM-DD hh:mm")
        return HttpResponseRedirect(reverse('games'))

    try:
        p1 = Player.objects.get(user_name=p1)
        p2 = Player.objects.get(user_name=p2)
    except Player.DoesNotExist:
        messages.add_message(request, messages.ERROR, "Player name does not exist.")
        return HttpResponseRedirect(reverse('games'))

    if p1.sign_off != s1 or p2.sign_off != s2:
        messages.add_message(request, messages.ERROR, "Incorrect signoff!")
        return HttpResponseRedirect(reverse('games'))

    g = Game(
            time_played=t,
            story=s,
            player1=p1,
            player2=p2,
            player1_before_game_elo=p1.elo_score,
            player2_before_game_elo=p2.elo_score,
            outcome=o
    )

    if o == Game.STALEMATES or o == Game.DRAWS or p1.id == p2.id:
        pass
    elif o == Game.CHECKMATES or o == Game.BRIBES:
        p1.elo_score += 1
        p2.elo_score -= 1
    else:
        messages.add_message(request, messages.ERROR, "Unsupported outcome.")
        return HttpResponseRedirect(reverse('games'))

    try:
        g.save()
        p1.save()
        p2.save()
    except ValidationError:
        messages.add_message(request, messages.ERROR, "Validation error.")
        return HttpResponseRedirect(reverse('games'))

    messages.add_message(request, messages.SUCCESS, "Successfully added!")
    return HttpResponseRedirect(reverse('games'))


def players(request):
    players = Player.objects.order_by('full_name')
    return render(request, 'elonomics/players.html', {
        'players': players
    })


def player(request, user_name):
    player = get_object_or_404(Player, user_name=user_name)
    games = (player.player1.all() | player.player2.all()).order_by('-time_played')
    return render(request, 'elonomics/player.html', {
        'player': player,
        'games': games
    })
