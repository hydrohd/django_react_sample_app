from django.shortcuts import render
from rest_framework  import generics, status
from rest_framework.response import Response
from .models import Quiz, Question, Answer

from api.serializers.answer_serializer import AnswerSerializer
from api.serializers.question_serializer import QuestionSerializer
from api.serializers.quiz_serializer import QuizSerializer
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.

class ListCreateQuiz(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class RetrieveUpdateDestroyQuiz(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class ListCreateQuestion(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class RetrieveUpdateDestroyQuestion(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ListCreateAnswer(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class RetrieveUpdateDestroyAnswer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

# class QuizQuestion(APIView):

#     def get(self, request, format="None", **kwargs):
#         question = Question.objects.filter(quiz_id=kwargs["quiz_id"])
#         serializer = QuestionSerializer(question, many=True)

#         return Response(serializer.data)

#     def post(self, request, format=None, **kwargs):
#         quiz = Quiz.objects.get(id=kwargs["quiz_id"])
#         serializer = QuestionSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save(quiz=quiz)
#             return Response(
#                 {"message": "Question created successfully", "data": serializer.data},
#                 status= status.HTTP_201_CREATED
#             )
        

# class QuizQuestionDetail(APIView):

#     def get_object(self, pk):
#         try:
#             return Question.objects.get(id=pk)
#         except Question.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk, format=None):
#         question = self.get_object(pk)
#         serializer = QuestionSerializer(question)
#         return Response(serializer.data)
    
#     def patch(self, request, pk, format=None):
#         question = self.get_object(pk)
#         serializer = QuestionSerializer(question, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         question = self.get_object(pk)
#         question.delete()
#         return Response(
#                 {"message": "Question deleted successfully"},
#                 status= status.HTTP_204_NO_CONTENT
#             )