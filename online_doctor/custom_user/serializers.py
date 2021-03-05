from rest_framework import serializers
from custom_user.models import User

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
        
class CustomUserSerializer(serializers.ModelSerializer):
    userId = serializers.IntegerField(required=False)
    class Meta:
        model = User
        fields = ['userId','userPhoneNumber', 'userName' ,'userRole']
    write_only_fields = ['password']

