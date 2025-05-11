# Create your models here.
from common import Base
from django.db import models

class Account(Base):
    name = models.CharField(max_length=255)



# 姓名 手机号 id号 密码 