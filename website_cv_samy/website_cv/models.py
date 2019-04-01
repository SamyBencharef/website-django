from django.db import models

# Create your models here.

class ProfesionnalExperiences(models.Model):
    job = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    description = models.TextField(null=True)
    date_start = models.DateField()
    date_end = models.DateField()
    current = models.BooleanField(default=False)
    logo = models.CharField(max_length=250, blank=True, help_text='path to image')

    class Meta:
        db_table = 'jobs'
        ordering = ['-date_end', '-date_start']

    def __str__(self):
        return self.job

class PersonalInformation(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)

    title = models.CharField(max_length=40)
    description = models.TextField(null=True)


    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    linkedIN = models.CharField(max_length=30)
    gitHUB = models.CharField(max_length=30)
    skills = models.CharField(max_length=50)
    driving_license = models.CharField(max_length=20)

    photo = models.CharField(max_length=250, blank=True, help_text='path to image')

    class Meta:
        db_table = 'perso_info'

    def __str__(self):
        return self.first_name


class Education(models.Model):
    formation = models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    description = models.TextField(null=True)
    date_start = models.DateField()
    date_end = models.DateField()
    current = models.BooleanField(default=False)
    logo = models.CharField(max_length=250, blank=True, help_text='path to image')

    class Meta:
        db_table = 'education'
        ordering = ['-date_end', '-date_start']

    def __str__(self):
        return self.formation

class Skill(models.Model):
    expertise = models.CharField(max_length=30)
    details = models.TextField(null=True)

    class Meta:
        db_table = 'skill'

    def __str__(self):
        return self.formation


class Hobbie(models.Model):
    expertise = models.CharField(max_length=30)
    details = models.TextField(null=True)

    class Meta:
        db_table = 'hobbie'

    def __str__(self):
        return self.expertise