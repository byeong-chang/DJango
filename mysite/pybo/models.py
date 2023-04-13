from django.db import models
#스프링의 @Entity를 사용하여 회원가입 Class 생성했던 것과 유사함
# @Entity = DB에 저장되는 객체로 인식하는 어노테이션

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200) #문자열 길이를 제한할 때 사용
    content = models.TextField() # 문자열 제한이 없는 데이터 타입
    create_date = models.DateTimeField() # 날짜와 시간

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content