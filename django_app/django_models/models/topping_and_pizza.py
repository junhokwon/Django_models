from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Pizza(models.Model):
    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        # 자신이 가지고있는 토핑목록을 뒤에 출력
        # ex) 치즈피자 (치즈, 토마토소스)
        # return self.name

        # toppings_string = ''
        # for topping in self.toppings.all():
        #     toppings_string += topping.name
        #     toppings_string += ', '
        # # 치즈, 토마토소스,
        #
        # toppings_string = toppings_string[:-2]
        # return '{} ({})'.format(
        #     self.name,
        #     toppings_string
        # )

        # str.join, list comprehension을 사용해서 한 줄로 줄이기
        # 리스트 컴프리헨션으로 다음과같은 리스트 생성 ['치즈', '토마토소스']
        # str.join메서드로 리스트를 문자열로 합침
        # 이후 결과를 리턴
        return '{} ({})'.format(self.name, ', '.join([t.name for t in self.toppings.all()]))

    class Meta:
        ordering = ('name',)