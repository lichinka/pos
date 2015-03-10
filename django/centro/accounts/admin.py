from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from accounts.models import UserProfile

#
# Unregister the default User admin application,
# because we built a custom user profile
# 
admin.site.unregister (User)
 
class UserProfileInline (admin.StackedInline):
    model = UserProfile
 
class UserProfileAdmin (UserAdmin):
    inlines = [UserProfileInline]


#
# Now register everything in the admin
# 
admin.site.register (User, UserProfileAdmin)

