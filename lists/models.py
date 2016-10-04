from django.core.urlresolvers import reverse
from django.db import models

from authtools.models import User
# Create your models here.

class List(models.Model):

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text