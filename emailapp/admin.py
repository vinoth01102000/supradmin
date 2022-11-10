from django.contrib import admin
from .models import User

admin.site.register(User)
# # Register your models here.
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# from api.models import Project

#
# new_group, created = Group.objects.get_or_create(name='new_group')
# # Code to add permission to group ???
# ct = ContentType.objects.get_for_model(Project)
# # Now what - Say I want to add 'Can add project' permission to new_group?
# UPDATE: Thanks for the answer you provided. I was able to use that to work out what I needed. In my case, I can do the following:

new_group, created = Group.objects.get_or_create(name='admin ')
proj_add_perm = Permission.objects.get(name='Can add project')
new_group.permissions.add(proj_add_perm)

new_group, created = Group.objects.get_or_create(name='Standard User')
proj_add_perm = Permission.objects.get(name='Can add project')
new_group.permissions.add(proj_add_perm)


new_group, created = Group.objects.get_or_create(name='Limited Access User')
proj_add_perm = Permission.objects.get(name='Can add project')
new_group.permissions.add(proj_add_perm)


new_group, created = Group.objects.get_or_create(name='Super admin')
proj_add_perm = Permission.objects.get(name='Can add project')
new_group.permissions.add(proj_add_perm)

