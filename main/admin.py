from django.contrib import admin
from parler.admin import TranslatableAdmin
from unfold.admin import ModelAdmin

from .models import Income, Expense


@admin.register(Income)
class IncomeAdmin(TranslatableAdmin, ModelAdmin):
    list_display = ("id", "get_source", "amount", "date", "user")
    list_filter = ("date",)
    search_fields = ("translations__source",)
    ordering = ("-created_at",)

    def get_source(self, obj):
        return obj.safe_translation_getter("source", any_language=True)
    get_source.short_description = "Source"


@admin.register(Expense)
class ExpenseAdmin(TranslatableAdmin, ModelAdmin):
    list_display = ("id", "get_source", "amount", "date", "user")
    list_filter = ("date",)
    search_fields = ("translations__source",)
    ordering = ("-created_at",)

    def get_source(self, obj):
        return obj.safe_translation_getter("source", any_language=True)
    get_source.short_description = "Source"
