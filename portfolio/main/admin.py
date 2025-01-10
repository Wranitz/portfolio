from django.contrib import admin
from .models import Project, Tag, ProjectImage

# creating a custom admin class for the tag model to display the name of the tag in the admin panel

class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title", "link"
        )
    inlines = []
    search_fields = ("title", "description")
    list_filter = ("tag",)
