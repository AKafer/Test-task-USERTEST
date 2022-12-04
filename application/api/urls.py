from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import GroupViewSet, TestViewSet, QuestionViewSet, AnswerViewSet, ResultViewSet

router = DefaultRouter()

router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'tests', TestViewSet, basename='tests')
router.register(r'questions', QuestionViewSet, basename='questions')
router.register(r'answers', AnswerViewSet, basename='answers')
router.register(r'rezults', ResultViewSet, basename='rezults')

urlpatterns = [
    path('', include(router.urls)),
]