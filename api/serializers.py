from rest_framework import serializers
from .models import IFSC


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = IFSC
        fields = ('BANK', 'IFSC', 'BRANCH', 'CENTRE', 'DISTRICT', 'STATE', 'ADDRESS', 'CONTACT', 'IMPS', 'RTGS', 'CITY', 'NEFT', 'MICR', 'UPI')