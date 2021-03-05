from django.contrib import admin
from .models import Chamber, Location


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'locationId','locationAdderssDetail', 'latitude', 'longitude'
    )
    def longitude(self, obj):
        return obj.locationLongitude
    def latitude(self, obj):
        return obj.locationLatitude

class ChamberAdmin(admin.ModelAdmin):
    list_display =(
        'chamberId','chamber_phone_number','chamber_name','address'
    )
    search_fields =[
        'chamberUserId__userName', 'chamberUserId__userPhoneNumber'
    ]
    
    def chamber_name(self,obj):
        return obj.chamberUserId.userName

    def chamber_phone_number(self,obj):
        return obj.chamberUserId.userPhoneNumber

    def address(self,obj):
        return obj.chamberLocationId.locationAdderssDetail

    chamber_name.admin_order_field='chamberUserId__userName'
    chamber_phone_number.admin_order_field = 'chamberUserId__userPhoneNumber'

admin.site.register(Chamber, ChamberAdmin)
admin.site.register(Location, LocationAdmin)