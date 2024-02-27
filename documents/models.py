from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class DocCategory(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name
    
class Document(models.Model):
    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    doccategory = models.ForeignKey(DocCategory, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description
    