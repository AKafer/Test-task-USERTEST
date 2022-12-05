from django.contrib import admin

from .models import Group, Test, Question, Answer, Result


class AnswerInline(admin.TabularInline):
    """Вспомогательный класс для отображения ответов в модели Question"""
    model = Answer
    extra = 0


class GroupAdmin(admin.ModelAdmin):
    """Класс отображения в админке групп"""
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'
    

class TestAdmin(admin.ModelAdmin):
    """Класс отображения в админке вопросов"""
    list_display = ('id', 'name', 'group')
    list_display_links = ('id', 'name', 'group')
    search_fields = ('name', 'group')
    list_filter = ('name', 'group')
    empty_value_display = '-пусто-'
    

class QuestionAdmin(admin.ModelAdmin):
    """Класс отображения в админке тестов"""
    inlines = (AnswerInline,)
    list_display = ('id', 'question', 'number', 'test')
    list_display_links = ('id', 'question', 'number', 'test')
    search_fields = ('question', 'number', 'test')
    list_filter = ('question', 'number', 'test')
    empty_value_display = '-пусто-'
    

class ResultAdmin(admin.ModelAdmin):
    """Класс отображения в админке результатов"""
    list_display = ('id', 'user', 'question', 'test', 'correct')
    list_display_links = ('id', 'user', 'question', 'test', 'correct')
    search_fields = ('user', 'question', 'test', 'correct')
    list_filter = ('user', 'question', 'test', 'correct')
    empty_value_display = '-пусто-'
    

admin.site.register(Group, GroupAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Result, ResultAdmin)
