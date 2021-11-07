from django.db import models
from django.db.models.deletion import CASCADE
from accounts.models import *
class agent(models.Model):
    agent = models.ForeignKey(User, on_delete=CASCADE,  related_name="root_agent")
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


class CompanyInfo(models.Model):
    company_owner = models.OneToOneField(agent, on_delete=CASCADE, related_name="company_root",)
    company_name = models.CharField(max_length=156, null=True, blank=True)
    primary_logo = models.ImageField(upload_to='company/logo')
    primary_background = models.ImageField(upload_to='company/background', null=True, blank=True)
    short_description = models.TextField(max_length=200, null=True, blank= True)

    def __str__(self):
       
        return self.company_owner.agent.company_name+"'s info"

    # def save(self, *args, **kwargs):
    #     if not self.company_name:
    #         self.company_name = User.company_name

    def save(self, *args, **kwargs):
         if not self.company_name:
            self.company_name = self.company_owner.agent.company_name
            return super().save(*args,**kwargs)
        
@receiver(post_save, sender=agent)
def create_company_profile(sender, instance, created, **kwargs):
    if CompanyInfo.objects.filter(company_owner = instance).exists() == False:
        if created == True:
            CompanyInfo.objects.create(company_owner = instance)

division_list = (
("Chattogram", "Chattogram" ), 
("Rajshahi", "Rajshahi") , 
("Khulna" , "Khulna" ) , 
("Barishal" , "Barishal"), 
("Sylhet" , "Sylhet" ), 
("Dhaka", "Dhaka" ), 
("Rangpur", "Rangpur") , 
("Mymensingh", "Mymensingh"),
)
class companyHotel(models.Model):
    host_company = models.ForeignKey(CompanyInfo, on_delete=CASCADE, related_name="root_host")
    title = models.CharField(max_length=100)
    cover_image= models.ImageField(upload_to='company/post_image', null=True, blank=True)
    location =  models.CharField(max_length=15, choices=division_list, null=True)

    def __str__(self):
        return self.title

choice_list = (
    ('single', "Single"),
    ('double', "Double")
    )

class room(models.Model):
    rel_hotel = models.ForeignKey(companyHotel, on_delete=CASCADE, related_name="root_hotels")
    title = models.CharField(max_length=30, null=True, blank= True)
    image = models.ImageField(upload_to='hotel/room', null=True, blank=True)
    type =  models.CharField(max_length=15, choices=choice_list, null=True)
    facilities = models.TextField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.FloatField(null= True, blank=True)

    booked_by = models.ManyToManyField(User, null=True, blank=True)

    def __str__(self):
        return self.title