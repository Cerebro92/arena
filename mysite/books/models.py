from django.db import models

# Create your models here.
class Publisher(models.Model):
	name = models.CharField(maxlength=30)
	address = models.CharField(maxlength=50)
	city = models.CharField(maxlength=60)
	state_province = models.CharField(maxlength=30)
	country = models.CharField(maxlength=50)
	website = models.URLField()
