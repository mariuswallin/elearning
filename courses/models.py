from django.core.urlresolvers import reverse
from django.db import models

from students.models import User


class Course(models.Model):
    name = models.CharField(max_length=200)
    students = models.ManyToManyField(User)

    def get_absolute_url(self):
        return reverse('course_detail', args=(self.id, ))

    def __str__(self):
        return self.name


class Section(models.Model):
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=100)
    number = models.IntegerField()
    text = models.TextField()

    class Meta:
        unique_together = ('course', 'number', )

    def __str__(self):
        return self.title


class Question(models.Model):
    section = models.ForeignKey(Section)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=1000)
    correct = models.BooleanField()

    def __str__(self):
        return self.text


class UserAnswer(models.Model):
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answer)
    user = models.ForeignKey(User)

    class Meta:
        unique_together = ('question', 'user',)
