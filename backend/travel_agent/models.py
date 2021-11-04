from django.db import models
from django.db.models.deletion import CASCADE
from accounts.models import *
class tagent(models.Model):
    agent = models.ForeignKey(User, on_delete=CASCADE)
    on_review = models.BooleanField(default=False)
    on_hold = models.BooleanField(default=False)
    suspended = models.BooleanField(default=False)

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.agent.email