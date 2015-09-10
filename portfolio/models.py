from django.db import models
from django.utils import timezone




class Skill(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=400)
	current_project = models.BooleanField(default=False)
	date_undertaken = models.DateField(default=timezone.now)
	link = models.CharField(max_length = 200)
	thumbnail = models.ImageField(default='http://placehold.it/700x300')
	tag_name = models.CharField(max_length=100)
	skills_list = models.ManyToManyField(Skill)
	code_link = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.title



