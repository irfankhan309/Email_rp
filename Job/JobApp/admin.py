from django.contrib import admin
from JobApp.models import Test_Form
# Register your models here.

class Test_Admin(admin.ModelAdmin):
    list_display=['Name','Email']


admin.site.register(Test_Form,Test_Admin)
