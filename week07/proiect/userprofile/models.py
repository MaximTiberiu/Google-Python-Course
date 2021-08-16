from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserExtend(User):
    customer = models.ForeignKey('aplicatie2.Companies', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.customer.name}'
