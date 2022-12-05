from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Group(models.Model):
    """
    Класс набор.
    """
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
    
    
class Test(models.Model):
    """
    Класс тест.
    """
    name = models.CharField(max_length=50)
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='group')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class Answer(models.Model):
    """
    Класс Ответ.
    """
    name = models.CharField(max_length=150)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name 
    

class Question(models.Model):
    """
    Класс вопрос.
    """
    question = models.TextField(max_length=150)
    number = models.PositiveIntegerField()
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='test')
    answers = models.ManyToManyField(
        Answer,
        # through='AnswerCheck',
        related_name='answers',
        verbose_name='ответы'
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.question
        

class Result(models.Model):
    """
    Класс результат.
    """
    correct = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_result')
    answer = models.ForeignKey(
        Answer,
        on_delete=models.CASCADE,
        related_name='answer_result')
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='test_result')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.correct    

# class AnswerCheck(models.Model):
#     """
#     Класс Ответ.
#     """
#     answer = models.ForeignKey(
#         Answer,
#         on_delete=models.CASCADE,
#         related_name='check_answer')
#     question = models.ForeignKey(
#         Question,
#         on_delete=models.CASCADE,
#         related_name='check_question')
#     correct = models.BooleanField(default=False)

    
#     class Meta:
#         ordering = ['id']

#     def __str__(self):
#         return str(self.id)
    


   


