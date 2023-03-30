from django.db import models

# Create your models here.

class Organization(models.Model):
    Organization_name = models.CharField(max_length=300, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)


class Token(models.Model):
    parent_organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    number_of_users = models.CharField(max_length=200, blank=True, null=True)
    expiration_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=False, blank=False)