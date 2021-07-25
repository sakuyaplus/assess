from django.contrib import admin

# Register your models here.
from .models import Discussion

class DiscussionAdmin(admin.ModelAdmin):
    list_display=('user_id','user_name','comment_date')
    list_display_links=('user_id','user_name')
    list_per_page=20

admin.site.register(Discussion,DiscussionAdmin)