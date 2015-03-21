from django.http import HttpResponse


def scoreboard(request):
    response = HttpResponse("Chess scoreboard")
    response.status_code = 501 # Not Implemented
    return response


def history(request):
    response = HttpResponse("Chess history")
    response.status_code = 501 # Not Implemented
    return response


def players(request):
    response = HttpResponse("List of players")
    response.status_code = 501 # Not Implemented
    return response


def player(request, user_name):
    response = HttpResponse("Chess stats for " + user_name)
    response.status_code = 501 # Not Implemented
    return response


def support(request):
    response = HttpResponse("Support")
    response.status_code = 501 # Not Implemented
    return response
