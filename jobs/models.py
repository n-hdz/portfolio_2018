from django.db import models

class Job(models.Model):
    """ Describes individual past Jobs to display in CV"""
    # Title
    title = models.CharField(verbose_name='job title', max_length=50)
    # Thumbnail for Job
    image = models.ImageField(verbose_name='thumbnail', upload_to='img/jobs')
    # Job description
    summary = models.CharField(verbose_name='description', max_length=140)
    # Job copy text
    copy = models.TextField(verbose_name='copy', null=True)
    # Date of Job
    date = models.DateTimeField(verbose_name='date of job', null=True)
    # Link to
    link = models.URLField(verbose_name='link to project', blank=True)

    def __str__(self):
        return self.title