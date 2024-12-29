from django.db import models

class U1(models.Model):
    msg1 = models.CharField(max_length=450)
   
class U2(models.Model):
    msg2 = models.CharField(max_length=450)
   