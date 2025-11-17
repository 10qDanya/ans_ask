from .models import Question
from rest_framework import generics
from questions.serializers import QuestionSerializer, QuestionRetrieveSerializer

class QuestionListApiView(generics.ListAPIView):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionCreateApiView(generics.CreateAPIView):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionRetrieveApiView(generics.RetrieveAPIView):
    
    queryset = Question.objects.all()
    serializer_class = QuestionRetrieveSerializer

class QuestionDestroyApiView(generics.DestroyAPIView):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer