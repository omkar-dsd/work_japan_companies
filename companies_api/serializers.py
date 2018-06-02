from django.contrib.auth.models import User, Group
from companies_api.models import *
from rest_framework import serializers


class PostalAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostalAddress
        fields = ('postal_code', 'locality', 'city', 'state')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'building_number', 'postal_code')
