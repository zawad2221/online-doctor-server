from django.contrib import admin
from .models import Test, TestType, TestReport

admin.site.register(TestReport)
admin.site.register(Test)
admin.site.register(TestType)
