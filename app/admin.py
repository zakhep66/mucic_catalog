from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Composition, Category, Group, Artist, Role

for i in [Category, Group, Artist, Role]:
	admin.site.register(i)


class CompositionResource(resources.ModelResource):
	class Meta:
		model = Composition


class CompositionAdmin(ImportExportModelAdmin):
	resource_class = CompositionResource


admin.site.register(Composition, CompositionAdmin)
