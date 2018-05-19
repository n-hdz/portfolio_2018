from django.db import models

class Job(models.Model):
    """ Describes individual past Jobs to display in CV"""
    # Title
    title = models.CharField(verbose_name='job title', max_length=50)
    # Thumbnail for Job
    image = models.ImageField(verbose_name='thumbnail', upload_to='img/')
    # Job description
    summary = models.CharField(verbose_name='description', max_length=140)
    # Date of Job
    date = models.DateTimeField(verbose_name='date of job', null=True)
    # Link to
    link = models.URLField(verbose_name='link to project', blank=True)