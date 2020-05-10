from django.contrib import admin
from . import models


@admin.register(models.Wiki)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "text",
        "update_date",
        "writer",
    )

    search_fields = ("^title",)
