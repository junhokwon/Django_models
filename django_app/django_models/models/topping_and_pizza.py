from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering =('name',)

class Pizza(models.Model):
    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        # ex) 치즈피자(치즈,토마토소스)
        # return self.name
        #
        # toppings_string = ''
        # for topping in self.toppings.all():
        #      toppings.string += topping.name
        #      toppings_string += ','
        #
        #
        #
        # toppings_string += toppings_string[:-2]
        # return '{} ({})'.format(
        #     self.name,
        #     toppings_string,
        # )
        return '{} ({})'.format(self.name,','.join([t.name for t in self.toppings.all()]))


    class Meta:
        ordering = ('name',)
