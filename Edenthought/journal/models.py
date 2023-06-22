



from django.db import models

from django.contrib.auth.models import User



class Thought(models.Model):
    title = models.CharField(max_length=85)
    content = models.CharField(max_length=300)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Thought ** title {self.title} / content {self.content} / date_posted {self.date_posted} / user {self.user}'
    


class Profile(models.Model):
    profile_pic = models.ImageField(null=True, blank=True, default='default.png')
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'#{self.id} - {self.user}'