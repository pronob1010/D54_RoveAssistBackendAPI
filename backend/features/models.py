from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class postExtra(models.Model):
    title = models.CharField(max_length=30)
    cover_image= models.ImageField(upload_to='company/post_image', null=True, blank=True)
    description = models.TextField(max_length=10000, null= True, blank=True)

    latitude = models.CharField(max_length=50, null= True, blank=True)
    longitude = models.CharField(max_length=50, null= True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title



from accounts. models import *
class addPlace(postExtra):
    user = models.ForeignKey(User, on_delete= CASCADE)

class addRestaurant(postExtra):
    user = models.ForeignKey(User, on_delete= CASCADE)

from travel_agent. models import *
class packageTour(postExtra):
    host = models.ForeignKey(agent, on_delete=CASCADE)
    entry = models.ManyToManyField(User, default=None, null=True, blank=True)

