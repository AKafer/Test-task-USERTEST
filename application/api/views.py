from django_filters import rest_framework as dfilters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
import requests
from bs4 import BeautifulSoup
from rest_framework.response import Response
import random

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
    
    @action(
        methods=['get'],
        detail=False,
        url_path=r'new_test')
    def get_data(self, request):
        print('***test***')
        url = 'https://centrevraz.ru/dlya-rvp-vnzh'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        questions = soup.find_all('div', {'class' : 'test_t'})
        new_group = Group.objects.get_or_create(name='новая группа')
        new_test = Test.objects.get_or_create(name='новый тест', group=new_group[0])
        answers = Answer.objects.all()
        for answer in answers:
            if answer.id > 46:
                answer.delete()
        i = 0
        for question in questions:
            i += 1
            q = str(question.find('b')).strip('<b></b>')
            new_q = Question.objects.get_or_create(
                question = q,
                number = i,
                test = new_test[0]
            )
            answers = question.find_all('span')
            right_ans = random.randint(1, len(answers))
            j = 0
            for ans in answers:
                j += 1
                ans_to_bd = str(ans).strip('<span></span>')
                correct = False
                if j == right_ans:
                    correct = True
                new_ans = Answer.objects.get_or_create(
                    name = ans_to_bd,
                    question = new_q[0],
                    correct = correct
                )
        new_ques = Question.objects.filter(test=new_test[0])
        serializer = QuestionSerializer(new_ques, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
        
        
        
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
