from django.db import models

# Create your models here.

class TranslationHistory(models.Model):
    text_to_translate = models.TextField(verbose_name="翻訳元テキスト")
    translated_text = models.TextField(verbose_name="翻訳結果")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
