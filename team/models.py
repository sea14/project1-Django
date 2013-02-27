from django.db import models

# Create your models here.
class Team(models.Model):
	teamName = models.CharField(unique = True, max_length=50)
	wins = models.CharField(max_length = 3)
	losses = models.CharField(max_length = 3)
	coach = models.CharField(max_length = 50)
	members = models.ManyToManyField(Member)
	class Meta(object):
		verbose_name_plural = "Teams"	

class Member(models.Model):
	name = models.CharField(unique = False, max_length=50)
	number = models.CharField(unique = True, max_length=3)
	grade = models.CharField(max_length=12)
	bio = models.CharField(max_length = 140)
	class Meta(object):
		verbose_name_plural = "Members"
		#ordering = ("name")

	def __unicode__(self):
		return U'%s %s' %(self.name, self.grade)
	
