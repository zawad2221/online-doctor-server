
from rest_framework import serializers
from .models import Pathology
from custom_user.models import User
from chamber.serializers import RelatedFieldAlternative
from chamber.models import Location
from chamber.serializers import LocationSerializer
from custom_user.serializers import CustomUserSerializer

class PathologySerializers(serializers.ModelSerializer):
    pathologyId = serializers.IntegerField(required=False)
    pathologyLocation = RelatedFieldAlternative(queryset=Location.objects.all(),serializer=LocationSerializer, source='pathologyLocationId')
    pathologyUser = RelatedFieldAlternative(queryset=User.objects.all(), serializer=CustomUserSerializer, source='pathologyUserId')
    class Meta:
        model = Pathology
        fields = ['pathologyId','pathologyLocation','pathologyUser']
    read_only_fields = ('pathologyLocation','pathologyUser')