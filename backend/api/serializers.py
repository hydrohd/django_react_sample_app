from rest_framework import serializers
from .models import Answer, Question, Quiz

class QuizSerializer(serializers.ModelSerializer):
    question_count = serializers.SerializerMethodField("get_question_count")

    class Meta:
        model = Quiz
        field = [
            'id',
            'title',
            'created_at',
            'question_count'
        ]

    def get_question_count(self, obj):
        return obj.question_count
    

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        field = [
            'id',
            'answer_text',
            'is_right'
        ]

class QuestionSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only = True)
    answers = AnswerSerializer(many = True)
    class Meta:
        model = Question
        field = [
            'id',
            'quiz',
            'title',
            'created_at',
            'answers'
        ]

    def create(self, validated_data):
        answer_data = validated_data.pop('answers', [])
        question = Question.objects.create(**validated_data)

        for answer in answer_data:

            Answer.objects.create(question = question, **answer)

    def update(self, instance, validated_data):
        instance.title = validated_data.pop('title', instance.title)
        
        #Update the relevant answers
        answers_data = validated_data.pop('answers', [])
        instance.answers.all().delete() #Deleting eisting answers
        for answer in answers_data:
            Answer.objects.create(question = instance, **answer)

        instance.save()

        return instance