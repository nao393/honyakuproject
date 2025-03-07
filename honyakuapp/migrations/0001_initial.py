# Generated by Django 4.0 on 2025-01-04 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TranslationHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_to_translate', models.TextField(verbose_name='翻訳元テキスト')),
                ('translated_text', models.TextField(verbose_name='翻訳結果')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
            ],
        ),
    ]
