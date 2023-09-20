from django.db import models
from datetime import datetime


# Create your models here.


class Todo(models.Model):
    title = models.CharField('todo', max_length=70)
    description = models.TextField('description')
    # date_created = models.DateTimeField('date and time created')
    # date_created = datetime.datetime.utcnow()
    date_created = models.DateTimeField('date and time created', default=datetime.now())
    date_to_complete = models.DateField('date to be completed')
    is_done = models.BooleanField('is task done', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/"

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Список дел'

