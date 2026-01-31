from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Transaction(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    
    class Meta :
        ordering = ['-created_at']
        
    def __str__(self):
        return self.text
