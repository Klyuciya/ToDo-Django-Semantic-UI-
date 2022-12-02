from django.db import models

# Create your models here.

class ToDo(models.Model):
    title = models.CharField('Task name', max_length=500)
    is_complete = models.BooleanField('Completed', default=False)
    # user = models.CharField('Name', max_length=50)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title