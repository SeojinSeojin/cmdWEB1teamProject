from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "genre",
        "pub_date",
        "edit_date",
    )

    list_filter = ("genre",)

    search_fields = ("^title",)