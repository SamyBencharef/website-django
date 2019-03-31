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
