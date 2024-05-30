from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User 
# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE =[
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('PL','PLAIN'),
        ('EL','ELACHI')
    ]
    name = models.CharField(max_length=100)
    image= models.ImageField(upload_to="chai/")
    date_added= models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default="")
    price = models.CharField(max_length=2, default=0)

    def __str__(self):
        return self.name
    

#one to many

class ChaiReview(models.Model):
    RATINGS = [(1, 1), (2,2), (3,3), (4,4), (5,5)]
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='review')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATINGS)
    comments = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
       return f'{self.user.username} review for {self.chai.name}'
   
# many to many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location =  models.CharField(max_length=100)
    chai_variety = models.ManyToManyField(ChaiVariety, related_name="stores")

    def __str__(self):
        return self.name
    
# one to one

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name="certificate")
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_date = models.DateTimeField()

    def __str__(self):
     return f'Certificate for {self.chai.name}'
    