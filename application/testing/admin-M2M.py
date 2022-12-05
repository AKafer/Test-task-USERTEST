from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError

from .models import Group, Test, Question, Answer, Result


# class AnswerCheckInline(admin.TabularInline):
#     """Вспомогательный класс для отображения ответов в модели Question"""
#     model = Answer
#     extra = 0


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
    

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('id', 'question', 'number', 'test', 'answers')
        
    def clean(self):
        cleaned_data = super(QuestionForm, self).clean()
        answers = cleaned_data.get('answers')
        true_list = []
        false_list = []
        for answer in answers:
            true_list.append(answer.correct)
            false_list.append(not answer.correct)
        if all(true_list):
            raise ValidationError(u'Все ответы не могу быть правильными')
        if all(false_list):
            raise ValidationError(u'Хотя бы один ответ должен быть правильным')
        return cleaned_data
    

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Класс отображения в админке тестов"""
    form = QuestionForm
    inlines = (AnswerCheckInline,)
    list_display = ('id', 'question', 'number', 'test')
    list_display_links = ('id', 'question', 'number', 'test')
    search_fields = ('question', 'number', 'test')
    list_filter = ('question', 'number', 'test')
    empty_value_display = '-пусто-'
    

class AnswerAdmin(admin.ModelAdmin):
    """Класс отображения в админке ответов"""
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'
    

# class AnswerCheckAdmin(admin.ModelAdmin):
#     """Класс отображения в админке ответов"""
#     list_display = ('id', 'answer', 'question', 'correct')
#     list_display_links = ('id', 'answer', 'question', 'correct')
#     search_fields = ('answer', 'question', 'correct')
#     list_filter = ('answer', 'question', 'correct')
#     empty_value_display = '-пусто-'

    
class ResultAdmin(admin.ModelAdmin):
    """Класс отображения в админке результатов"""
    list_display = ('id', 'user', 'answer', 'test', 'correct')
    list_display_links = ('id', 'user', 'answer', 'test', 'correct')
    search_fields = ('user', 'answer', 'test', 'correct')
    list_filter = ('user', 'answer', 'test', 'correct')
    empty_value_display = '-пусто-'
    

admin.site.register(Group, GroupAdmin)
admin.site.register(Test, TestAdmin)
# admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
# admin.site.register(AnswerCheck, AnswerCheckAdmin)
admin.site.register(Result, ResultAdmin)
