from django.db import models
from rest_framework import permissions
from django.contrib.auth import get_user_model

# Create your models here.
class Fundraiser(models.Model):
   title = models.CharField(max_length=200)
   description = models.TextField()
   goal = models.IntegerField()
   image = models.URLField()
   is_open = models.BooleanField()
   date_created = models.DateTimeField(auto_now_add=True) 
   owner = models.ForeignKey(
      get_user_model(),
      related_name='owned_fundraiser', 
      on_delete=models.CASCADE
   )

class Pledge(models.Model):
   amount = models.IntegerField()
   comment = models.CharField(max_length=200)
   anonymous = models.BooleanField()
   fundraiser = models.ForeignKey(
      'Fundraiser',
      related_name='pledges', 
      on_delete=models.CASCADE
   )
   owner = models.ForeignKey(
      get_user_model(),
      related_name='pledges', 
      on_delete=models.CASCADE
   )

class IsOwnerOrReadOnly(permissions.BasePermission):

   def has_object_permission(self, request, view, obj):
      # Allow read-only access for any request
      if request.method in permissions.SAFE_METHODS:
         return True
      # Only allow write access if the user is the owner
      return obj.owner == request.user

