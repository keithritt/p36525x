from django.contrib import admin
from .models import UserProfile, Exercise, Set, Goal, Group

'''
class ApiAdmin(admin.ModelAdmin):
    fieldsets = [
        #('ID',   {'fields': ['id']}),
        ('Lookup', {'fields': ['lookup']}),
        ('Display', {'fields': ['display']}),
    ]
    #inlines = [ChoiceInline]
    list_display = ('id', 'lookup', 'display')
    #list_filter = ['pub_date']
    #search_fields = ['question_text']
'''
admin.site.register(UserProfile)
admin.site.register(Exercise)
admin.site.register(Set)
admin.site.register(Goal)
admin.site.register(Group)