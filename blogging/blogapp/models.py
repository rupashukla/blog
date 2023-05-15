from django.db import models

# Create your models here.
class Blog(models.Model):
    blogid = models.TextField(max_length=100, blank=False, null=False, default='')
    blogtitle = models.TextField(blank=True, null=True)
    description = models.TextField(max_length=100, blank=False, null=False)
    Content = models.TextField(max_length=100, blank=False, null=False)


class User(models.Model):
    UserId = models.TextField(max_length=100, blank=False, null=False)
    name = models.TextField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    password = models.TextField(max_length=100, blank=False, null=False)

class Like(models.Model):
    likeid = models.TextField(max_length=100, blank=False, null=False)
    Userid = models.ForeignKey(User, on_delete=models.CASCADE)
    blogid = models.ForeignKey(Blog, on_delete=models.CASCADE)


