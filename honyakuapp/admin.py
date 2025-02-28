from django.contrib import admin
from .models import TranslationHistory

@admin.register(TranslationHistory)
class TranslationHistoryAdmin(admin.ModelAdmin):
    list_display = ('text_to_translate', 'translated_text', 'created_at')
    search_fields = ('text_to_translate', 'translated_text')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    fields = ('text_to_translate', 'translated_text')
    readonly_fields = ('created_at',)
