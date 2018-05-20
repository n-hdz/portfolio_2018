from django.db import models

class Blog(models.Model):
    """ Describes individual Blog entries """
    # Title for Blog entry
    title = models.CharField(verbose_name="entry title", max_length=50)
    # Date for Blog entry
    date = models.DateField(verbose_name="entry timestamp")
    # Thumbnail for Blog entry
    image = models.ImageField(verbose_name="entry thumbnail", upload_to='img/blogs')
    # Blog description
    summary = models.TextField(verbose_name="entry body")