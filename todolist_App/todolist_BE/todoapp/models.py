from django.db import models

# Create your models here.
class Todo(models.Model):
    id=models.AutoField(primary_key=True)#auto_increment 
    userid=models.CharField(max_length=100)
    title=models.CharField(max_length=50)
    done=models.BooleanField(default=False)
    regdate=models.DateTimeField(auto_now_add=True) # 작성날짜
    moddate=models.DateTimeField(auto_now_add=True) # 수정날짜
    
    