from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime as dt

# Create your models here.
# A model for each skill
#   With: skill, skill level (x of 5), more?

# A model for each job
#   With: title, company, description, time_from, time_to

class SuperSkill(models.Model):
    name = models.CharField(max_length=64)
    level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.level:
            ...
        elif self.level > 5:
            self.level = 5
        elif self.level < 0:
            self.level = 0
        
        super(SuperSkill, self).save(*args, **kwargs)
    
class Skill(models.Model):
    name = models.CharField(max_length=64)
    level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    superskill = models.ForeignKey(SuperSkill, null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.level > 5:
            self.level = 5
        elif self.level < 0:
            self.level = 0
        
        super(Skill, self).save(*args, **kwargs)

class Education(models.Model):
    year_start = models.IntegerField(validators=[MinValueValidator(1992), MaxValueValidator(dt.now().year)], default=None)
    year_end = models.IntegerField(validators=[MinValueValidator(1992), MaxValueValidator(dt.now().year)], null=True, blank=True, default=None)
    degree = models.CharField(max_length=256)
    school = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.degree
    
class Work(models.Model):
    year_start = models.IntegerField(validators=[MinValueValidator(1992), MaxValueValidator(dt.now().year)], default=None)
    year_end = models.IntegerField(validators=[MinValueValidator(1992), MaxValueValidator(dt.now().year)], null=True, blank=True, default=None)
    title = models.CharField(max_length=128)
    work_place = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    