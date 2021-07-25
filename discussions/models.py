from django.db import models
from datetime import datetime
# Create your models here.
class Discussion(models.Model):

    user_id=models.IntegerField() #评论用户ID
    user_name=models.CharField(max_length=30) #评论用户名
    message = models.TextField(blank=True) #评论内容
    comment_date = models.DateTimeField(default=datetime.now) #评论日期
    
    def __str__(self):
        return self.user_name