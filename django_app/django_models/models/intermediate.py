from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    # current_club 프로퍼티에 현재속하는 Club리턴
    # current_tradeinfo프로퍼티에 현재 자신의 tradeinfo리턴

class Club(models.Model):
    name = models.CharField(max_length=40)
    players = models.ManyToManyField(
        Player,
        through='TradeInfo',
    )

    def __str__(self):
        return self.name

    def squad(self,year=None):
        pass

    # squard메서드에 현재선수들만 리턴
    # 인수로 년도를 받아 해당년도의 현직선수들을 리턴
    # 주어지지않으면 현재를 기준으로 함

class TradeInfo(models.Model):
    player = models.ForeignKey(Player,on_delete=models.CASCADE)
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    date_joined = models.DateField()
    date_leave = models.DateField(null=True,blank=True)

    #1. 프로퍼티로 is_current 속성이 TradeInfo가 현직인지 여부 반환
    #2. recommender와 prev_club을 활성화 시키고 Club