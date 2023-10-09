from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    MALE = "m"
    FEMALE = "f"
    OTHER = "o"
    
    GENDER_CHOICES =(
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "other"),
    )

    
    id = models.PositiveBigIntegerField(primary_key=True)
    profile_pic = models.ImageField(upload_to="image/users", blank=True, null=True)
    phone = models.CharField(max_length=10, unique=True)
    Address = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
    )
    dob = models.DateField()