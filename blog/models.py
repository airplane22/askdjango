import re

from django.conf import settings
from django.db import models
from django.forms import ValidationError
# Create your models here.
from django.urls import reverse


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    # 길이 제한이 있는 문자열-Charfield

    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )

    #author = models.CharField(max_length=20) #migration-option2에서 default or 1에서 입력안될때 default anonymous, 입력되면 입력값
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='제목',
                             help_text='포스팅 제목을 입력해주세요.(100자 내외)')
    content = models.TextField(verbose_name='내용')            #길이 제한이 없는 문자열-Textfield
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
                              validators=[lnglat_validator], help_text='경도,위도 포맷으로 입력')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True) #field에서 relation 지정할때 문자열로(뒤에 있을때??) 다른모델일때 - 앱이름.클래스이름
    created_at = models.DateTimeField(auto_now_add=True) #날짜와 시간을 저장 (처음 생겼을때 일시저장autonowadd)
    updated_at = models.DateTimeField(auto_now=True) #날짜와 시간을 저장(바뀔때마다 시간 저장 autonow)

    class Meta:
        ordering = ['-id'] #필드옵션 여러개 줄수있지만 한두개가 query 성능 높여줌


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)   #post_id field 생성
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name