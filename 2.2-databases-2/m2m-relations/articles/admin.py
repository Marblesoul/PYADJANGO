from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 1
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_count += 1
        if main_count > 1:
            raise ValidationError('Основной тег может быть только один')
        super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1
    verbose_name = 'Тег'
    verbose_name_plural = 'Теги'
    fields = ['topic', 'is_main']
    autocomplete_fields = ['topic']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    list_display = ['title', 'published_at']
    search_fields = ['title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']