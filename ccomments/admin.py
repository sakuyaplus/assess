from django.contrib import admin

# Register your models here.
from .models import CComment

class CCommentAdmin(admin.ModelAdmin):
    list_display=('user_id','user_name','course_id','stars','message','comment_date')
    list_display_links=('user_id','user_name',"course_id","stars")
    list_per_page=20

admin.site.register(CComment,CCommentAdmin)