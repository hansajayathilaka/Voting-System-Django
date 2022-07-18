from django.contrib.auth.models import User
from django.db import models


class Election(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField()
    StartDate = models.DateTimeField()
    EndDate = models.DateTimeField()
    IsActive = models.BooleanField(default=True)
    ContractAddress = models.CharField(max_length=100)
    IsRegistered = models.BooleanField(default=False)


class Candidate(models.Model):
    Name = models.CharField(max_length=150)
    Age = models.IntegerField(null=True, blank=True)
    Party = models.CharField(max_length=100, null=True, blank=True)
    Website = models.URLField(max_length=200, null=True, blank=True)
    Election = models.ForeignKey(Election, on_delete=models.CASCADE)


class Vote(models.Model):
    Voter = models.ForeignKey(User, on_delete=models.CASCADE)
    Candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    Election = models.ForeignKey(Election, on_delete=models.CASCADE)
    Created_At = models.DateTimeField(auto_now_add=True)
