from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'first'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    timeForFullMoney = models.FloatField(initial=0)
    timeForFullMoney1 = models.IntegerField(initial=0)
    timeForFullMoney2 = models.IntegerField(initial=0)
    timeForHalfMoney =  models.FloatField(initial=0)
    timeForHalfMoney1 = models.IntegerField(initial=0)
    timeForHalfMoney2 = models.IntegerField(initial=0)
    timeSpendForChoice = models.FloatField(initial=0)
    timeSpendForChoice1 = models.IntegerField(initial=0)
    timeSpendForChoice2 = models.IntegerField(initial=0)
    timeSpendForDraw = models.FloatField(initial=0)
    timeSpendForDraw1 = models.IntegerField(initial=0)
    timeSpendForDraw2 = models.IntegerField(initial=0)
    choice = models.IntegerField(initial = 0)
    draw = models.IntegerField(initial = 0)
    name = models.StringField()
    number = models.StringField()
    money = models.IntegerField(initial=50)
    drawofchoice = models.IntegerField(initial=0)
    pass
