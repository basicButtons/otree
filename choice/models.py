from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""



class Constants(BaseConstants):
    name_in_url = 'choice'
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
    choice1 = models.IntegerField()
    choice2 = models.IntegerField()
    choice3 = models.IntegerField()
    choice4 = models.IntegerField()
    choice11 = models.IntegerField()
    choice12 = models.IntegerField()
    choice21 = models.IntegerField()
    choice22 = models.IntegerField()
    choice31 = models.IntegerField()
    choice32 = models.IntegerField()
    choice41 = models.IntegerField()
    choice42 = models.IntegerField()
    cost1 = models.IntegerField()
    cost2 = models.IntegerField()
    cost3 = models.IntegerField()
    cost4 = models.IntegerField()
    money = models.IntegerField(initial = 50)