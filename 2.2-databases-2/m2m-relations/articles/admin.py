from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleScope


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        tag_count = 0
        all_tags = []
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                tag_count += 1
            if form.cleaned_data.get('tag'):
                all_tags.append(form.cleaned_data.get('tag').id)
        if len(all_tags) > len(set(all_tags)):
            raise ValidationError('Тэги не должны повторяться!')
        if tag_count > 1:
            raise ValidationError('Основным может быть только один тэг!')
        elif tag_count == 0:
            raise ValidationError('Выберите основной тэг!')
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset
    extra = 4


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
