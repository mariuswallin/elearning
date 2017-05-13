from django.core.urlresolvers import reverse
from django.db import models

from students.models import Student


class Course(models.Model):
    name = models.CharField(max_length=200)
    students = models.ManyToManyField(Student)

    def get_absolute_url(self):
        return reverse('course_detail', args=(self.id, ))

    def __str__(self):
        return self.name
