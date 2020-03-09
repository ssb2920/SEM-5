from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,default=None)
    content = models.TextField(default='content')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    #entries = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
class Entry(models.Model):
    id1 = models.ForeignKey(Post,on_delete=models.CASCADE,default=None,)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    rollno = models.IntegerField(default=0)
    year = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    