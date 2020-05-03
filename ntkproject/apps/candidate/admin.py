from django.contrib import admin
from .models import Professional, Student

admin.site.site_header = 'АСУВ'

class CategoryAdmin(admin.ModelAdmin):
	list_filter = ("gender", "ready_to_move", "work_type", "type_education", "program", "qualification", )
	list_display = ("id", "last_name", "first_name","middle_name", "gender", "date_birth", "address", "ready_to_move", "email", "telephone", "type_education", "program", "qualification", "work_type", "work_post",  "upload", )
	search_fields = ("id", "last_name", "first_name", "middle_name", "gender", "date_birth", "address", "ready_to_move", "email", "telephone", "type_education", "program", "qualification", "work_type", "work_post",   )
	readonly_fields=("upload",)



admin.site.register(Professional, CategoryAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_filter = ("gender", "praktika", "university", "institute", "specialty", "year_of_begin", "year_of_end", )
	list_display = ("id", "last_name", "first_name","middle_name", "gender", "date_birth", "email", "telephone", "praktika", "university", "institute", "specialty", "year_of_begin", "year_of_end", )
	search_fields = ("id", "last_name", "first_name", "middle_name", "gender", "date_birth", "email", "telephone", "praktika", "university", "institute", "specialty", "year_of_begin", "year_of_end", )

admin.site.register(Student, CategoryAdmin)

