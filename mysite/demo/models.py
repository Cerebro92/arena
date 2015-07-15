from django.db import models

class Author(models.Model):
	def __unicode__(self):
		return self.name
	id = models.AutoField('ID', primary_key=True)
	name = models.CharField(max_length=50,null=True)
	email = models.EmailField(max_length=40,null=True)
	password = models.CharField(max_length=20,null=True)

class Article(models.Model):
	def __unicode__(self):
		return self.article_title
	author_name = models.CharField(max_length=50)
	article_title = models.CharField(max_length=20,null=True)
	article_content = models.TextField()
