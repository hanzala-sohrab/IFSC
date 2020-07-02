from django.db import models


# Create your models here.
class IFSC(models.Model):
    BANK = models.CharField(max_length=50, null=False)
    IFSC = models.CharField(max_length=12, null=False)
    BRANCH = models.CharField(max_length=100, null=False, default='Foo')
    CENTRE = models.CharField(max_length=50, null=False)
    DISTRICT = models.CharField(max_length=50, null=False)
    STATE = models.CharField(max_length=50, null=False)
    ADDRESS = models.CharField(max_length=1000, null=False)
    CONTACT = models.CharField(max_length=15, null=False)
    IMPS = models.CharField(max_length=6, null=True)
    RTGS = models.CharField(max_length=6, null=True)
    CITY = models.CharField(max_length=50, null=False)
    NEFT = models.CharField(max_length=6, null=True)
    MICR = models.CharField(max_length=18, null=True)
    UPI = models.CharField(max_length=6, null=True)

    def __str__(self):
        return self.BANK
