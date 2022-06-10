from django.db import models


class User(models.Model):
	name = models.CharField(max_length = 30)
	email = models.CharField(max_length = 30, null = True)
	creation_date = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name


class Posts(models.Model):
	title = models.CharField(max_length = 30)
	content = models.TextField()
	created_at = models.DateTimeField(null= True, blank = True)
	updated_at = models.DateTimeField(null = True, blank = True)
	user = models.ForeignKey(User,related_name='cards', on_delete = models.CASCADE)

	def __str__(self):
		return self.title 
