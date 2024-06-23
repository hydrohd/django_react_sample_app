from rest_framework import serializers
from api.serializers.answer_serializer import AnswerSerializer
from api.models import Quiz, Question


class SimpleQuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many = True)

    class Meta:
        model = Question
        fields = [
            'id',
            'title',
            'created_at',
            'answers'
        ]

class QuizSerializer(serializers.ModelSerializer):
    question_count = serializers.SerializerMethodField("get_question_count")
    questions = SimpleQuestionSerializer(many = True)
    class Meta:
        model = Quiz
        fields = [
            'id',
            'title',
            'created_at',
            'questions',
            'question_count'
        ]

    def get_question_count(self, obj):
        return obj.question_count