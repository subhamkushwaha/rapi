from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    password=models.TextField(max_length=10)
    address=models.TextField()
    def __str__(self) -> str:
        return self.name
