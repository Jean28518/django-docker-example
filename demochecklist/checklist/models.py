from django.db import models

# Create your models here.

class Task(models.Model):
    done = models.BooleanField(default=False)
    task_title = models.CharField(max_length=200)
    task_description = models.CharField(max_length=2048)
    
    # def __str__(self):
    #     return self.task_text
    