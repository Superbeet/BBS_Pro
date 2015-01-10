from django.contrib import admin
from app01 import models


class BBS_admin(admin.ModelAdmin):
    list_display = ('title','summary','author','signature' ,'view_count', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title','author__user__username') #Foreign key
    
    # Inner function to show signature of a certain user
    def signature(self,obj):
        return obj.author.signature
    
    signature.short_description = 'New Signature'
    
# Register your models here.
admin.site.register(models.BBS, BBS_admin)
admin.site.register(models.Category)
admin.site.register(models.BBS_user)

