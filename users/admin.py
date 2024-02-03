from django.contrib import admin
from django.contrib.auth.models import Group

from users.models import User, UserConfirmation


admin.site.unregister(Group)


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']


admin.site.register(User, UserAdmin)
admin.site.register(UserConfirmation)
