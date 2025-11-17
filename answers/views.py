from rest_framework import generics
from .models import Answer
from .serializers import AnswerSerializer

class AnswerCreateApiView(generics.CreateAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerRertieverApiView(generics.RetrieveAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerDestroyAoiView(generics.DestroyAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer