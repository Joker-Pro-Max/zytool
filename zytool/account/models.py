# Create your models here.
from common import Base
from django.db import models


class Account(Base.BaseModel):
    username = models.CharField(max_length=255)
    iphone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'account_model'

    def __str__(self):
        return self.username

