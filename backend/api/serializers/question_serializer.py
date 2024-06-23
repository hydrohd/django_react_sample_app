from rest_framework import serializers
from api.models import Question, Answer
from api.serializers.quiz_serializer import QuizSerializer
from api.serializers.answer_serializer import AnswerSerializer

class QuestionSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only = True)
    answers = AnswerSerializer(many = True)
    
    class Meta:
        model = Question
        fields = [
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