from django.db import models

# Create your models here.
class Text(models.Model):

    __tablename__ = 'Text'

    filename = models.CharField(max_length=80)
    text = models.TextField()
    file_path = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.filename