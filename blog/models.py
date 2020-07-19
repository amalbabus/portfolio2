from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


class BlogModel(models.Model):

    blog_title = models.CharField(max_length=30)
    blog_time = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='blog/images/', default=False)
    blog_description = RichTextUploadingField()

    def __str__(self):
        return self.blog_title
    


    

 