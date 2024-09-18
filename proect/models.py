from django.contrib.auth.models import User
from django.db import models

class Proect(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()
    cat = models.ForeignKey("Category", models.PROTECT)
    user = models.ForeignKey(User, models.CASCADE, verbose_name="user")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name