from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "genre",
        "onlyMonthDay",
        "writer",
    )

    list_filter = ("genre",)

    search_fields = ("^title",)
