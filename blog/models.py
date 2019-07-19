import re
from django.db import models
from django.forms import ValidationError
# Create your models here.


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


    author = models.CharField(max_length=20) #migration-option2에서 default or 1에서 입력안될때 default anonymous, 입력되면 입력값
    title = models.CharField(max_length=100, verbose_name='제목',
                             help_text='포스팅 제목을 입력해주세요.(100자 내외)')
    content = models.TextField(verbose_name='내용')            #길이 제한이 없는 문자열-Textfield
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
                              validators=[lnglat_validator], help_text='경도,위도 포맷으로 입력')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True) #날짜와 시간을 저장 (처음 생겼을때 일시저장autonowadd)
    updated_at = models.DateTimeField(auto_now=True) #날짜와 시간을 저장(바뀔때마다 시간 저장 autonow)

    class Meta:
        ordering = ['-id'] #필드옵션 여러개 줄수있지만 한두개가 query 성능 높여줌


    def __str__(self):
        return self.title