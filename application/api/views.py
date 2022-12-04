from django_filters import rest_framework as dfilters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from testing.models import Group, Test, Question, Answer, Result

# from .filters import TagOperatorFilter
from .serializers import GroupSerializer, TestSerializer, QuestionSerializer, AnswerSerializer, ResultSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """Класс представления клиентов"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    

class TestViewSet(viewsets.ModelViewSet):
    """Класс представления клиентов"""
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('group', )
    

class QuestionViewSet(viewsets.ModelViewSet):
    """Класс представления клиентов"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('test', )
    
class AnswerViewSet(viewsets.ModelViewSet):
    """Класс представления клиентов"""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('question', )
    
    
class ResultViewSet(viewsets.ModelViewSet):
    """Класс представления клиентов"""
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
