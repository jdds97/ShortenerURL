import random
import string
from django.db import models

# Create your models here.
class URL(models.Model):
    id=models.AutoField(primary_key=True, editable=False)
    url = models.URLField(max_length=200)
    shortCode = models.CharField(max_length=10, editable=False, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    accessCount = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.shortCode:
            self.shortCode = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.shortCode