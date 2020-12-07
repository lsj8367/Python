from django.contrib import admin
from myfriend.models import Friend

# Register your models here.
#admin.site.register(Friend)

class FriendAdmin(admin.ModelAdmin):
    list_display = ('id', 'irum', 'juso', 'nai')
     
admin.site.register(Friend, FriendAdmin)