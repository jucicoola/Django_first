from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin

#Question이라는 테이블 생성하고 models의 값을 인자로 받음 
#table이라함은 엑셀 같은 것으로 보면 됨 
#question은 엑셀 파일명으로 생각하면 됨 
#CharField, DateTimeField 2개의 열 값에 해당함 장고에서 id 라는 열을 만들어서 1, 2, 3,
#여기에서 행 위치 값의 주소를 알 수 있음 
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    
       
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    def __str__(self):
       return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text