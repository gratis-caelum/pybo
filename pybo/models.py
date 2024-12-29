from django.db import models

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200) # 최대 200자 까지, 제목처럼 글자 수가 제한된 텍스트는 CharField를 사용
    content = models.TextField() # 글자 수에 제한이 없는 텍스트는 TextField 사용
    create_date = models.DateTimeField() # 날짜와 시간 정보를 저장하는 속성은 DateTimeField 사용
    
    # id 값 대신 제목을 표시할 수 있음
    def __str__(self):
        return self.subject
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 기존 모델을 속성으로 연결하기 위해 ForeignKey 사용 (두 모델 간의 관계를 정의할 때 사용)
    # on_delete = models.CASCADE : 답변이 연결된 질문이 삭제되면, 해당 답변도 함께 삭제된다는 의미를 가짐
    content = models.TextField() # 
    create_date = models.DateTimeField()