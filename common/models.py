from django.db import models


class GradeBase(models.IntegerChoices):
    FIRST = 1, 'First'
    SECOND = 2, 'Second'
    THIRD = 3, 'Third'
    FOURTH = 4, 'Fourth'
    FIFTH = 5, 'Fifth'
    SIXTH = 6, 'Sixth'
    SEVENTH = 7, 'Seventh'
    EIGHTH = 8, 'Eighth'
    NINTH = 9, 'Ninth'
    TENTH = 10, 'Tenth'
    ELEVENTH = 11, 'Eleventh'


class Grade(models.Model):
    base = models.IntegerField(choices=GradeBase.choices, default=GradeBase.FIRST)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.base} {self.name}'
