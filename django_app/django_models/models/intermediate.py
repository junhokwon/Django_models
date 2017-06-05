from datetime import timezone

from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


    # current_club프로퍼티에 현재 속하는 Club리턴
    # club_set을 사용하여 Player에서 클럽을 가져올 수 있다.(역참조
    # 해당선수의 가입 일자가 현재보다 이전이고, 떠난적이 없을
    @property
    def current_club(self):
        return self.club_set.get(
            tradeinfo__date_joined__lte = timezone.now(),
            tradeinfo__date_leaved=None
        ).name

    # current_tradeinfo프로퍼티에 현재 자신의 TradeInfo리턴
    # 1번은 역참조를 활용하여 player의 tradeinfo를 찾아낸다.
    (1) @property
    def current_tradeinfo(self):
        return self.tradeinfo_set.get(player=self)

    # 2번은 함수를 활용하여 player의 tradeinfo를 찾아낸다.

    (2) @property
    def current_tradeinfo(self):
        return TradeInfo.objects.get(
            player_id=self.id,
            tradeinfo__date_joined__lte = timezone.now(),
            tradeinfo__date_leaved = None,

        )





class Club(models.Model):
    name = models.CharField(max_length=40)
    players = models.ManyToManyField(
        Player,

        through='TradeInfo',
    )
    prev_club = models.ManyToManyField(
        Club,
        through=TradeInfo
    )
    recommender = models.ManyToManyField(
        Player,
        through=TradeInfo
    )

    def __str__(self):
        return self.name
    # Club's name.players.all() : players인스턴스는 MTOM일때 사용할 수 있다.

    def squad(self, year=None):
        if year is None:
            return self.players.filter(
                tradeinfo__date_joined = timezone.now())
        else:
            base_year_query = TradeInfo.objects.filter(
                date_joined__lte = timezone.datetime(year,1,1),
                date_leaved__lte = timezone.datetime(year,12,31),
            )
            club_year_query = TradeInfo.objects.filter(
                date_joined__lte = timezone.datetime(year,1,1),
                date_leaved__lte = None,
            )
            club_year_query_string = ''
            for club_year_query in base_year_query:
                club_year_query_string += club_year_query.name
                club_year_query_string += ','
                return club_year_query_string




        # squad메서드에 현직 선수들만 리턴
        # 인수로 년도(2017, 2015...등)를 받아
        # 해당 년도의 현직 선수들을 리턴,
        # 주어지지 않으면 현재를 기준으로 함


class TradeInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date_joined = models.DateField()
    date_leaved = models.DateField(null=True, blank=True)
    recommender = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)
    prev_club = models.ForeignKey(Club,on_delete=models.CASCADE, null=True,blank=True)
    # 2. recommender와 prev_club을 활성화시키고 Club의 MTM필드에 through_fields를 명시


    # 1. property로 is_current 속성이 TradeInfo가 현재 현직(leaved하지 않았는지)여부 반환

    @property
    # 여기서 self는 인스턴스로 인스턴스 = TradeInfo.objects.create(~~)로 생성했거나 tradeinfo_set.create(~~)로 생성한것이다.
    def is_current(self):
        return self.date_leaved is None






# 위의 요구조건들을 만족하는 실행코드 작성