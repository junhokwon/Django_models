from django.db import models
from .car import Car

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()




    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    def __str__(self):
        return "Homegroup {}\'s student ({},{})".format(
                self.home_group,
                self.name,
                self.age,
        )

class Teacher(CommonInfo):
    classes = models.CharField(max_length=20)

    def __str__(self):
            return 'class {} \'s teacher ({},({})'.format(
                self.classes,
                self.name,
                self.age
            )

