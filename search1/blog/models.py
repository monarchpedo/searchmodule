from django.db import models

# Create your models here.
class Post(models.Model):
 	title = models.CharField(max_length = 140)
 	body = models.TextField()
 	date = models.DateTimeField()

 	def __str__(self):
 		return  self.title

class Image(models.Model):
    word1 = models.TextField()
    link = models.URLField()
    link2 = models.ImageField()
    visitno1 = models.BigIntegerField()
    time1 = models.DateTimeField() 
      
    def __str__(self):
        return self.link2


class web(models.Model):
     word = models.TextField()
     link = models.URLField()
     visitno = models.BigIntegerField()
     time = models.DateTimeField()
#     session = models.DurationField()

     def __unicode__(self):
      	  return str(self.link)


class video(models.Model):
     word = models.TextField()
     link = models.URLField()
     link3 = models.FileField()
     visitno = models.BigIntegerField()
     time = models.DateTimeField()
     #session = models.DurationField()    	

     def __str__(self):
     	return self.link3

     































