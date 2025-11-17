from django.urls import path

from answers.apps import AnswersConfig
from answers.views import AnswerCreateApiView, AnswerRertieverApiView, AnswerDestroyAoiView

app_name = AnswersConfig.name

urlpatterns = [
    path('', AnswerCreateApiView.as_view(), name='create_answer'),
    path('retrieve/<int:pk>/', AnswerRertieverApiView.as_view(), name='retrieve_answer'),
    path('destroy/<int:pk>/', AnswerDestroyAoiView.as_view(), name='destroy_answer'),
]
