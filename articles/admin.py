from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            if form.cleaned_data['is_main']:
                counter += 1
        if counter > 1:
            raise ValidationError('Основным может быть только 1 раздел')
        elif counter < 1:
            raise ValidationError('Выберите основной тег')
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 2

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
