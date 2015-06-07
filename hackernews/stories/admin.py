from django.contrib import admin
from stories.models import Story


class StoryAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'domain', 'moderator', 'createdat', 'updatedat')
    list_filter = ('createdat', 'updatedat')
    search_fields = ('title', 'moderator__username', 'moderator__first_name', 'moderator__last_name')

    fieldsets = [
            (Story, {
                'fields' : ('title', 'url', 'points')
            }),
            ('Moderator',{
                'classes' : ('collapse',),
                'fields' : ('moderator',)
            }),
            ('Change History', {
                'classes' : ('collapse',),
                'fields' : ('createdat', 'updatedat')
            })
            ]
    readonly_fields = ('createdat', 'updatedat')

# Register your models here.
admin.site.register(Story, StoryAdmin)
