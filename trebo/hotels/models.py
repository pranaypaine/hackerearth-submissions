from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Hotel(models.Model):
	name = models.TextField()
	image = models.ImageField(upload_to="post_images/",
		null=True,
		blank=True)
	rating = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(5.0)])
	link = models.TextField()
	actual_price = models.FloatField()
	discount = models.IntegerField(default=0)
	location = models.TextField()
	
	"""docstring for Post"""
	
	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title