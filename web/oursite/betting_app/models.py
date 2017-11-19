from django.db import models

class Player(models.Model):

    pid = models.IntegerField(default = 0)
    player_name = models.CharField(max_length = 32, default = "")
    wins = models.IntegerField(default = 0)
    losses = models.IntegerField(default = 0)
    wallet = models.IntegerField(default = 0)
    amount_bet = models.IntegerField(default = 0)
    team_bet = models.CharField(max_length = 3, default = "")

    def __str__(self):
        return "PID: {}\n# Wins: {}\n# Loses: {}\nWallet: {}\nAmount Bet: {}\nTeam Bet: {}\n".format(self.pid, self.wins, self.losses, self.wallet, self.amount_bet, self.team_bet)

class Team(models.Model):
    team_name = models.CharField()
    team_id = models.IntegerField()
    rank = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()

    def team_id_to_str(self):
        return 0
        