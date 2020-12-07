from django.contrib import admin
from myguest.models import Guest

# Register your models here.
# 수정할때 drop을 먼저하고 하는게 좋다.
class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'regdate')
    
admin.site.register(Guest, GuestAdmin)