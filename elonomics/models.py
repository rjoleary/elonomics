from django.db import models


class Player(models.Model):
    user_name = models.SlugField(max_length=30, unique=True)
    full_name = models.CharField(max_length=30)
    sign_off = models.CharField(max_length=10)
    # The player's elo field is a cached result of iterating through all the
    # games. If a game is added with a out of order time, this field must be
    # computed from scratch.
    elo_score = models.IntegerField(default=0)

    def __str__(self):
        return "{} ({})".format(self.full_name, self.elo_score)


class Game(models.Model):
    time_played = models.DateTimeField()
    story = models.CharField(max_length=100,
            help_text="Use the format: In a long and adventurous battle...")
    player1 = models.ForeignKey('Player', related_name='player1')
    player2 = models.ForeignKey('Player', related_name='player2')
    player1_before_game_elo = models.IntegerField()
    player2_before_game_elo = models.IntegerField()

    CHECKMATES = 1
    STALEMATES = 2
    DRAWS = 3
    BRIBES = 4
    OUTCOME_CHOICES = (
            (CHECKMATES, 'checkmates'),
            (STALEMATES, 'stalemates'),
            (DRAWS, 'draws'),
            (BRIBES, 'bribes'),
    )
    outcome = models.IntegerField(choices=OUTCOME_CHOICES, default=CHECKMATES)

    def __str__(self):
        return "{} ({}) {} {} ({})".format(self.player1.full_name,
                self.player1_before_game_elo, self.get_outcome_display(),
                self.player2.full_name, self.player2_before_game_elo)
