from django.db import models
from django.core.urlresolvers import reverse

class Pokemon(models.Model):
	name        = models.CharField(max_length=300)
	type        = models.CharField(max_length=100)
	hability     = models.CharField(max_length=200)
	weight      = models.FloatField()
	height      = models.FloatField()
	description = models.CharField(max_length=300)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		view = "detail"
		return reverse (view, kwargs={"pk":self.id})

	def get_success_url_one(self):
		view = "delete"
		return reverse (view, kwargs={"pk":self.id})

	def get_success_url(self):
	 	view = "detail"
	 	return reverse (view, kwargs={"pk":self.id})

	def get_hit_url(self):
	 	view = "update"
	 	return reverse (view, kwargs={"pk":self.id})