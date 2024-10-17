from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	technology = models.CharField(max_length=20)
	start_date = models.DateField(auto_now_add=True)
	end_date = models.DateField(blank=True, null=True)
	is_active = models.BooleanField()
	
	def __str__(self):
		return self.name