from django.db import models

# Create your models here.


class Test_Form(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField()
