from django.db import models

#Question이라는 테이블 생성하고 models의 값을 인자로 받음 
#table이라함은 엑셀 같은 것으로 보면 됨 
#question은 엑셀 파일명으로 생각하면 됨 
#CharField, DateTimeField 2개의 열 값에 해당함 장고에서 id 라는 열을 만들어서 1, 2, 3,
#여기에서 행 위치 값의 주소를 알 수 있음 
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        from django.utils import timezone
        import datetime
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text