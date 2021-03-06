from django.db import models
from django.utils import timezone


class Skill(models.Model):
    '''
    Stores a single skill
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    '''
    Stores a single project, related to :model:`Skill`
    '''
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    current_project = models.BooleanField(default=False)
    date_undertaken = models.DateField(default=timezone.now)
    link = models.CharField(max_length=200,
                            default='https://www.linkedin.com/in/rowanv')
    thumbnail = models.ImageField(default='http://placehold.it/700x300')
    tag_name = models.CharField(max_length=100)
    skills_list = models.ManyToManyField(Skill)
    code_link = models.CharField(max_length=200, null=True)
    order_by_integer = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class PastWorkEngagement(models.Model):
    """
    Stores a single work engagement.
    """
    description = models.CharField(max_length=400)


