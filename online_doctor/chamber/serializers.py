from django.db import models
from rest_framework import serializers

from .models import Chamber, Location
from custom_user.models import User
from custom_user.serializers import CustomUserSerializer

class RelatedFieldAlternative(serializers.PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = kwargs.pop('serializer', None)
        if self.serializer is not None and not issubclass(self.serializer, serializers.Serializer):
            raise TypeError('"serializer" is not a valid serializer class')

        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False if self.serializer else True

    def to_representation(self, instance):
        if self.serializer:
            return self.serializer(instance, context=self.context).data
        return super().to_representation(instance)


class LocationSerializer(serializers.ModelSerializer):
    locationId = serializers.IntegerField(required=False)
    class Meta:
        model = Location
        fields = '__all__'

class ChamberSerializer(serializers.ModelSerializer):

    chamberId = serializers.IntegerField(required = False)
    chamberLocation = RelatedFieldAlternative(queryset=Location.objects.all(), serializer=LocationSerializer,source='chamberLocationId')
    chamberUser = RelatedFieldAlternative(queryset=User.objects.all(), serializer=CustomUserSerializer, source='chamberUserId')
    
    class Meta:
        model = Chamber
        fields = ['chamberId','chamberLocation','chamberUser']

    read_only_fields = ('chamberLocation','chamberUser')