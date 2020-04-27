from django.db import models
from userApp.models import UserProfile

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class District(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Thana(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Category(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    title = models.CharField(max_length=255, verbose_name="Title")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title

class Organisation(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    about = models.TextField()
    org_category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)
    division = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    thana = models.ForeignKey(Thana, on_delete=models.SET_NULL, null=True)
    postal_area = models.CharField(max_length=255,null=True)
    phone = models.IntegerField()
    email = models.EmailField(max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    objects = models.QuerySet()

    def __str__(self):
        return f"{self.name}- {self.owner.email}" 

class orgDetail(models.Model):
    org_id = models.OneToOneField(Organisation, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images', null=True,blank = True) 
    logo = models.ImageField(upload_to = 'images', null=True,blank = True)
    description = models.TextField()
    facebook_url = models.URLField()
    twitter_url = models.URLField()
    youtube_url = models.URLField()
    website_url = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.org_id.name}- {self.description}" 

class orgProject(models.Model):
    name = models.CharField(max_length=255)
    organization_name = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    selected_area = models.CharField(max_length=255)
    details = models.TextField()
    duration = models.DateTimeField()
    project_image = models.ImageField(upload_to = 'images', null=True,blank = True) 
    budget = models.CharField(max_length=255)
    status = models.TextField(verbose_name="Status")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
