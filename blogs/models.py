from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    """The class that stores information from a blog."""
    name = models.CharField(max_length=50)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return the string representation of the blog name"""
        return f'{self.name}'


class Comment(models.Model):
    """The class that stores the user commment from a
    specific blog"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'comments'

    def __str__(self):
        """Return the string representation of the comment"""
        return f'{self.text[:30]}' if len(f'{self.text}') > 30 \
            else f'{self.text}'
