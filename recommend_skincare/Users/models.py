from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.hashers import make_password

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # store hashed password
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phoneNo = models.CharField(
        max_length=15,
        validators=[RegexValidator(
            regex=r'^\+?\d{9,15}$',
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )]
    )

    def save(self, *args, **kwargs):
        # Hash password before saving
        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username