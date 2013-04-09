from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(unique=True, max_length=100)
    # biodiversity stats
    birds_in_region = models.CharField(unique=False, max_length=100)
    protected_land = models.CharField(unique=False, max_length=25)
    # economic stats
    revenue = models.IntegerField(unique=False, max_length=25)
    income = models.IntegerField(unique=False, max_length=25)
    industry = models.CharField(unique=False, max_length=100)
    # education stats
    student_teacher_ratio = models.CharField(unique=False, max_length=25)
    teacher_salary = models.IntegerField(unique=False, max_length=25)
    literacy_rate = models.IntegerField(unique=False, max_length=25)
    # weather stats
    rainfall = models.IntegerField(unique=False, max_length=25)
    temperature = models.IntegerField(unique=False, max_length=25)
    humidity = models.IntegerField(unique=False, max_length=25)
    elevation = models.IntegerField(unique=False, max_length=25)
    # health stats
    distance_to_hospital = models.IntegerField(unique=False, max_length=25)
    percent_of_budget_allocated = models.IntegerField(unique=False, max_length=25)
    
    def __unicode__(self):
        return U'%s %s' %(self.income, self.name)
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(specificState, self).save(*args, **kwargs)


class Galapagos(models.Model):
    name = models.CharField(unique=True, max_length=100)
    # biodiversity stats
    birds_in_region = models.CharField(unique=False, max_length=100)
    protected_land = models.CharField(unique=False, max_length=25)
    # economic stats
    revenue = models.IntegerField(unique=False, max_length=25)
    income = models.IntegerField(unique=False, max_length=25)
    industry = models.CharField(unique=False, max_length=100)
    # education stats
    student_teacher_ratio = models.CharField(unique=False, max_length=25)
    teacher_salary = models.IntegerField(unique=False, max_length=25)
    literacy_rate = models.IntegerField(unique=False, max_length=25)
    # weather stats
    rainfall = models.IntegerField(unique=False, max_length=25)
    temperature = models.IntegerField(unique=False, max_length=25)
    humidity = models.IntegerField(unique=False, max_length=25)
    elevation = models.IntegerField(unique=False, max_length=25)
    # health stats
    distance_to_hospital = models.IntegerField(unique=False, max_length=25)
    percent_of_budget_allocated = models.IntegerField(unique=False, max_length=25)
    
    def __unicode__(self):
        return U'%s %s' %(self.income, self.name)
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(galapagos, self).save(*args, **kwargs)
