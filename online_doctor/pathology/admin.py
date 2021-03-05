from django.contrib import admin
from .models import Pathology

class PathologyAdmin(admin.ModelAdmin):
    list_display =(
        'pathologyId','pathology_phone_number','pathology_name','address'
    )
    search_fields =[
        'pathologyUserId__userName', 'pathologyUserId__userPhoneNumber'
    ]
    
    def pathology_name(self,obj):
        return obj.pathologyUserId.userName

    def pathology_phone_number(self,obj):
        return obj.pathologyUserId.userPhoneNumber

    def address(self,obj):
        return obj.pathologyLocationId.locationAdderssDetail

    pathology_name.admin_order_field='pathologyUserId__userName'
    pathology_phone_number.admin_order_field = 'pathologyUserId__userPhoneNumber'
admin.site.register(Pathology, PathologyAdmin)
