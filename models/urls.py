from django.urls import path, include
from .views import SectionListCreate, QuestionListCreate, CheckQuestionListCreate
urlpatterns = [
    path('', SectionListCreate),
    path('question/', QuestionListCreate),
    path('check-question/<id>/<answer>/', CheckQuestionListCreate),
]