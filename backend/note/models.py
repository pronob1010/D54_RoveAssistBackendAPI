from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
from accounts. models import User
class note(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(max_length=1200, null=True, blank=True)
    
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        
