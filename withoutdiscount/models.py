from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""



class Constants(BaseConstants):
    name_in_url = 'withoutdiscount'
    players_per_group = 3
    num_rounds = 1

    instructions_template = 'A/box4.html'

    url1 = '1.webm'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField()
    number = models.IntegerField()
    mytime1 = models.IntegerField(initial=0)
    mytime2 = models.IntegerField(initial=0)
    mytime3 = models.IntegerField(initial=0)
    mytime4 = models.IntegerField(initial=0)
    mytime5 = models.IntegerField(initial=0)
    mytime6 = models.IntegerField(initial=0)
    mytime7 = models.IntegerField(initial=0)
    mytime8 = models.IntegerField(initial=0)
    timeSpend1 = models.FloatField(initial = 0)
    timeSpend2 = models.FloatField(initial = 0)
    timeSpend3 = models.FloatField(initial = 0)
    timeSpend4 = models.FloatField(initial = 0)
    money = models.IntegerField(initial = 50)