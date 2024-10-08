"""
URL configuration for django_react_sample project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (
    ListCreateAnswer,
    ListCreateQuestion,
    ListCreateQuiz,
    RetrieveUpdateDestroyAnswer,
    RetrieveUpdateDestroyQuestion,
    RetrieveUpdateDestroyQuiz
)

urlpatterns = [
    path("quiz/", ListCreateQuiz.as_view(), name = 'quiz_List'),
    path("quiz/<int:quiz_id>", RetrieveUpdateDestroyQuiz.as_view(), name = "quiz_detail"),
    path("answer/", ListCreateAnswer.as_view(), name = 'answer_list'),
    path("answer/<int:answer_id>", RetrieveUpdateDestroyAnswer.as_view(), name = "answer_detail"),
    path("question/", ListCreateQuestion.as_view(), name = "question_list"),
    path("question/<int:question_id>", RetrieveUpdateDestroyQuestion.as_view(), name = "question_detail")
]
