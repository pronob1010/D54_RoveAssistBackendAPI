from django.db import models
from django.db.models.deletion import CASCADE
from accounts.models import *
class agent(models.Model):
    agent = models.ForeignKey(User, on_delete=CASCADE)
    on_review = models.BooleanField(default=False)
    on_hold = models.BooleanField(default=False)
    suspended = models.BooleanField(default=False)

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.agent.email

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_agent(sender, instance, created, **kwargs):
    if agent.objects.filter(agent= instance).exists() == False:
        if created == False and instance.is_agent == True:
            agent.objects.create(agent = instance)
