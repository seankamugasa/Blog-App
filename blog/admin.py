from django.contrib import admin
from django.contrib.admin.models import LogEntry, DELETION
from django.urls import reverse
from django.utils.html import escape
from django.utils.safestring import mark_safe
from .models import Post, Comment

# Project Models Registered.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    list_filter = ('status','created','publish','author')
    search_fields = ('title','body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','post','created','active')
    list_filter = ('active','created','updated')
    search_fields = ('name','email','body')
    

# This class is supposed to track user actions in the admin panel.
# Its mainly for user who have access to the Admin Panel.
# Log entry comes with Django installed, we just import it.
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'action_time'

    list_filter = [
        'user',            # This is the name of the user.
        'content_type',    # Shows the areas that the user has made changes too
        'action_flag'      # Represents the action done ie, modified, deleted, edited.
    ]

    search_fields = [
        'object_repr',    # Related to the user object where the search is based from.
        'change_message'  # The information displayed for user activity.
    ]

    list_display = [
        'action_time',    
        'user',
        'content_type',
        'object_link',  # Takes you where the user made changes.
        'action_flag',
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = '<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return mark_safe(link)
    object_link.admin_order_field = "object_repr"
    object_link.short_description = "object"