from rest_framework import serializers

from testing.models import Group, Test, Question, Answer, Result


class GroupSerializer(serializers.ModelSerializer):
    """Класс сериализатора групп."""

    class Meta:
        fields = '__all__'
        model = Group
        

class TestSerializer(serializers.ModelSerializer):
    """Класс сериализатора тестов."""

    class Meta:
        fields = '__all__'
        model = Test
        

class QuestionSerializer(serializers.ModelSerializer):
    """Класс сериализатора вопросов."""

    class Meta:
        fields = '__all__'
        model = Question
        
        
class AnswerSerializer(serializers.ModelSerializer):
    """Класс сериализатора ответов."""

    class Meta:
        fields = '__all__'
        model = Answer
        
        
class ResultSerializer(serializers.ModelSerializer):
    """Класс сериализатора результатов."""

    class Meta:
        fields = '__all__'
        model = Result