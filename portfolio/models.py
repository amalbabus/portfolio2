from django.db import models

class Project(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)


    def __str__(self):
        return self.title
    

class MessageModel(models.Model):

    name = models.CharField(blank=False,max_length=20)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False,max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
