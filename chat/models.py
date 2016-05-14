from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models



class Album23(models.Model):

    album_title = models.CharField(max_length=500)
    album_logo = models.CharField(max_length=1000)
    album_logo2 = models.FileField()
    def get_absolute_url(self):
        return reverse('chat:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.album_title 
