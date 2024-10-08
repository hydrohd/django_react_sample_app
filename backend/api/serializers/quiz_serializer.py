from rest_framework import serializers
from api.serializers.answer_serializer import AnswerSerializer
from api.models import Quiz, Question, Answer
from api.serializers.question_serializer import QuestionSerializer



class QuizSerializer(serializers.ModelSerializer):
    question_count = serializers.SerializerMethodField("get_question_count")
    questions = QuestionSerializer(many = True)

    class Meta:
        model = Quiz
        fields = [
            'id',
            'title',
            'author',
            'created_at',
            'questions',
            'question_count'
        ]

    def create(self, validated_data):
        questions_data = validated_data.pop('questions', [])
        quiz = Quiz.objects.create(**validated_data)
        
        for question_data in questions_data:
            
            question_data['quiz'] = quiz
            question_serializer = QuestionSerializer(data=question_data)
            question_serializer.is_valid(raise_exception=True)
            question_serializer.create(question_data)

        return quiz


    def get_question_count(self, obj):
        return obj.question_count