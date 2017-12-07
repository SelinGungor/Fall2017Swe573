from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    start_date = models.DateField(verbose_name='StartDate', default=timezone.now, blank=True)
    end_date = models.DateField(verbose_name='EndDate', default=timezone.now, blank=True)
    user = models.ForeignKey(User)

    def get_absolute_url(self):
        return reverse('analyse')

    class Meta:
        ordering = ['start_date']
