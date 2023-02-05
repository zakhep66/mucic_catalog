from django.contrib import admin

from .models import Composition, Category, Group, Artist, Role

admin.site.register(Composition)
admin.site.register(Category)
admin.site.register(Group)
admin.site.register(Artist)
admin.site.register(Role)
