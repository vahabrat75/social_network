from django.db import models
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone_number = PhoneNumberField("User phone number", unique=True)


class RequestLog(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="requests")
    ip = models.CharField("IP address",  max_length=250, default='0.0.0.0')
    path = models.CharField("Requested URL", max_length=250, null=True, blank=True)
    user_agent = models.CharField("Client's user agent", max_length=250, null=True, blank=True)
    request_method = models.CharField("Request method", max_length=10)
    created = models.DateTimeField('Request datetime', auto_now_add=True)

# Create your models here.
