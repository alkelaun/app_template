from django.db import models
from django.conf import settings
from crum import get_current_user
from django.urls import reverse

# Create your models here.
#User = settings.AUTH_USER_MODEL

# Create your models here.

### REFERENCES ###
#https://docs.djangoproject.com/en/4.0/topics/db/models/

'''
class DefaultModel(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name  #needs to be a string

    def get_absolute_url(self):
        return reverse("$URL_NAME_SPACE:$NAME", kwargs={"pk": self.pk})
'''

### ###