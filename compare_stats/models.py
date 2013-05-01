from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(unique=False, max_length=100)
    # biodiversity stats
    birds_in_region = models.CharField(unique=False, max_length=100)
    birds_in_region_text = models.CharField(unique=False, max_length=100)
    protected_land_image = models.CharField(unique=False, max_length=50)
    protected_land_percentage = models.CharField(unique=False, max_length=50)
    # economic stats
    revenue = models.CharField(unique=False, max_length=50)
    income = models.CharField(unique=False, max_length=50)
    income_text = models.CharField(unique=False, max_length=50)
    industry = models.CharField(unique=False, max_length=100)
    # education stats
    teacher = models.CharField(unique=False, max_length=50)
    student_teacher_ratio = models.CharField(unique=False, max_length=50)
    student_teacher_text = models.CharField(unique=False, max_length=50)
    teacher_salary = models.CharField(unique=False, max_length=50)
    literacy_rate = models.CharField(unique=False, max_length=50)
    # weather stats
    rainfall = models.CharField(unique=False, max_length=50)
    rainfall_text = models.CharField(unique=False, max_length=50)
    temperature = models.CharField(unique=False, max_length=50)
    humidity = models.CharField(unique=False, max_length=50)
    # health stats
    health_budget = models.CharField(unique=False, max_length=50)
    health_budget_text = models.CharField(unique=False, max_length=50)
    health_expenditure = models.CharField(unique=False, max_length=50)
    health_expenditure_text = models.CharField(unique=False, max_length=50)
    hospitals_per_person = models.CharField(unique=False, max_length=50)
    hospitals_per_person_text = models.CharField(unique=False, max_length=50)

    
    def __unicode__(self):
        return U'%s %s' %(self.income, self.name)
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(specificState, self).save(*args, **kwargs)
        


class Galapagos(models.Model):
    name = models.CharField(unique=True, max_length=100)
    # biodiversity stats
    birds_in_region = models.CharField(unique=False, max_length=100)
    birds_in_region_text = models.CharField(unique=False, max_length=100)
    protected_land_image = models.CharField(unique=False, max_length=50)
    protected_land_percentage = models.CharField(unique=False, max_length=50)
    # economic stats
    revenue = models.CharField(unique=False, max_length=50)
    income = models.CharField(unique=False, max_length=50)
    income_text = models.CharField(unique=False, max_length=50)
    industry = models.CharField(unique=False, max_length=100)
    # education stats
    teacher = models.CharField(unique=False, max_length=50)
    student_teacher_ratio = models.CharField(unique=False, max_length=50)
    student_teacher_text = models.CharField(unique=False, max_length=50)
    teacher_salary = models.CharField(unique=False, max_length=50)
    literacy_rate = models.CharField(unique=False, max_length=50)
    # weather stats
    rainfall = models.CharField(unique=False, max_length=50)
    rainfall_text = models.CharField(unique=False, max_length=50)
    temperature = models.CharField(unique=False, max_length=50)
    humidity = models.CharField(unique=False, max_length=50)
    # health stats
    health_budget = models.CharField(unique=False, max_length=50)
    health_budget_text = models.CharField(unique=False, max_length=50)
    health_expenditure = models.CharField(unique=False, max_length=50)
    health_expenditure_text = models.CharField(unique=False, max_length=50)
    hospitals_per_person = models.CharField(unique=False, max_length=50)
    hospitals_per_person_text = models.CharField(unique=False, max_length=50)
    
    def __unicode__(self):
        return U'%s %s' %(self.income, self.name)
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(galapagos, self).save(*args, **kwargs)
