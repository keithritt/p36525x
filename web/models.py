from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  dob = models.DateField(max_length=8)
  group = models.CharField(max_length=30)
  gender = models.CharField(max_length=1)

  def __str__(self):
    return self.user.username

class Exercise(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

class Set(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
  exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=False)
  reps = models.IntegerField(null=False)
  ts = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '{0} {1} {2}'.format(self.user.username, self.exercise.name, self.reps)

class Goal(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=False)
  reps = models.IntegerField(null=False)
  due_date = models.DateField(max_length=8)

  def __str__(self):
    return '{0} {1} {2} {3}'.format(self.user.username, self.exercise.name, self.count, self.due_date)

class Group(models.Model):
  name = models.CharField(max_length=30)
  user = models.ManyToManyField(User)

  def __str__(self):
    return self.name

class Weight(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
  weight = models.FloatField(null=False)
  ts = models.DateTimeField(auto_now_add=True)
