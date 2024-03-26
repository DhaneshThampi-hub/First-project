from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class  Commonuser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=20,null=True)
    resume=models.FileField(null=True)
    gender=models.CharField(max_length=10,null=True)
    type = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.user.username
    

class  Recruiter(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=20,null=True)
    image=models.FileField(null=True)
    gender=models.CharField(max_length=10,null=True)
    company = models.CharField(max_length=200,null=True)
    type = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.user.username
    

class Jobs(models.Model):
    recruiter = models.ForeignKey(Recruiter,on_delete=models.CASCADE)
    start_date =models.DateField()
    end_date =models.DateField()
    title=models.CharField(max_length=10)
    salary=models.FloatField(max_length=10)
    description = models.CharField(max_length=200)
    exp = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    creationdate= models.DateField()
    def __str__(self):
        return self.title
    


class Apply(models.Model):
    job = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    commonuser =models.ForeignKey(Commonuser,on_delete=models.CASCADE)
    resume =models.FileField(null=True)
    applydate =models.DateField()
    
    def __str__(self):
        return str(self.id)