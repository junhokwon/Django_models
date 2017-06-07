"""
Post모델
    author = User와 연결
    title
    content
    created_date
        DateTimeField사용
    modified_date
        DateTimeField사용
Comment모델
    post = Post와 연결
    author = User와 연결
    content
    created_date
    modified_date
User모델
    name
    created_date
    modified_date
"""
from django.db import models
from util.models.mixins import TimeStampedMixin


class Post(TimeStampedMixin):
    author = models.ForeignKey('User')
    title = models.CharField(max_length=50)
    content = models.TextField()


class Comment(TimeStampedMixin):
    post = models.ForeignKey(Post)
    author = models.ForeignKey('User')
    content = models.TextField()


class User(TimeStampedMixin):
    name = models.CharField(max_length=50)


"""
PostLike
    post = Post
    user = User
    created_date

Tag
    title

Post모델
    like_users = User와 MTM으로 연결, Intermediate model로 PostLike모델을 사용
    tags = MTM으로 Tag와 연결

    def like_post(self, user):
        return '해당 user의 PostLike를 생성, 이후 생성 객체를 리턴'
"""