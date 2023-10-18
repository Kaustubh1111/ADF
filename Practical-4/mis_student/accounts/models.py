from django.db import models

# Create your models here.
class suser(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    uname = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=20)

    def __str__(self):
         return self.uname

class Post(models.Model):
    author = models.ForeignKey(suser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(suser, related_name='post_likes', blank=True)
    comments = models.ManyToManyField(suser, through='Comment', related_name='post_comments', blank=True)

    def __str__(self):
        return f'{self.author.uname} - {self.created_at}'

class Comment(models.Model):
    user = models.ForeignKey(suser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.uname} - {self.post} - {self.created_at}'