from django.contrib import admin

from .models import Composition, Category, Group, Artist, Role

some_list = [Composition, Category, Group, Artist, Role]

for i in some_list:
    admin.site.register(i)
