from django.contrib import admin

from .models import User, Schools, SchoolsClassrooms


class SchoolsClassroomsAdmin(admin.TabularInline):
    model = SchoolsClassrooms
    extra = 0
    fields = ('class_number', 'class_letter')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name', 'last_name', 'user_school', 'user_classroom', 'user_gender')
    list_filter = ('user_school', 'user_gender')
    readonly_fields = ('user_id',)
    search_fields = ('user_id', 'user_school')


@admin.register(Schools)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'school_city')
    list_filter = ('school_name',)
    search_fields = ('school_name', 'school_city')
    inlines = (SchoolsClassroomsAdmin,)

