from django.db import models

# Create your models here.

class tboard(models.Model):
    b_no = models.IntegerField(default=0) 
    u_id = models.CharField(max_length=20)
    b_title = models.CharField(max_length=200)
    b_content = models.CharField(max_length=3000)
    b_date = models.DateField(auto_now=True)
    b_group =  models.IntegerField(default=0) 
    b_step =  models.IntegerField(default=0) 
    b_indent =  models.IntegerField(default=0) 
    b_hit =  models.IntegerField(default=0) 
    b_img =  models.CharField(max_length=200)
    
    def __str__(self):
        return self.b_title