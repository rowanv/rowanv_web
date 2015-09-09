from django.db import models
from django.utils import timezone

class Project(models.Model):
	title = models.CharField(max_length = 100)
	description = models.CharField(max_length = 400)
	current_project = models.BooleanField(default=False)
	date_undertaken = models.DateField(default=timezone.now)
	link = models.CharField(max_length = 200)
	thumbnail = models.ImageField(blank=True)

	def __str__(self):
		return self.title

