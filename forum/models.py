from django.db import models

class State(models.Model):
    name = models.CharField(max_length=80)    
    def __unicode__(self):
    	return self.name

class Constituency(models.Model):
    state = models.ForeignKey(State)
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=30)
    candidate = models.CharField(max_length=100)
    party = models.CharField(max_length=50)
    def __unicode__(self):
    	return self.name