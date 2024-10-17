from django.db import models

# Create your models here.
class Folder(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Name(models.Model):
    name_text = models.CharField(max_length=200, unique=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name_text