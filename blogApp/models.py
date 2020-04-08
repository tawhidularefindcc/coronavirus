from django.db import models

from userApp.models import UserProfile


class Blog(models.Model):
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=300)
    featured_img = models.ImageField(null=True, blank=True)
    description = models.TextField()
    blog_tag = models.ManyToManyField("Tag")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag_name = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag_name
