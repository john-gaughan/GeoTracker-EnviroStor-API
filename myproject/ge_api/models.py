from django.db import models

class HelloWorld(models.Model):
  greeting = models.CharField(max_length=60)
  language = models.CharField(max_length=20)

  def __str__(self):
    return self.language + ": " + self.greeting
