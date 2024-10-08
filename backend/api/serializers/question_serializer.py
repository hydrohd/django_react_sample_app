from rest_framework import serializers
from api.models import Question, Answer
from api.serializers.answer_serializer import AnswerSerializer

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many = True)
    
    class Meta:
        model = Question
        fields = [
            'id',
            'title',
            'created_at',
            'answers'
        ]

    def create(self, validated_data):
        answers_data = validated_data.pop('answers', [])
        question = Question.objects.create(**validated_data)

        for answer_data in answers_data:
            answer_data['question'] = question
            answer_serializer = AnswerSerializer(data=answer_data)
            answer_serializer.is_valid(raise_exception=True)
            answer_serializer.create(answer_data)

        return question

    def update(self, instance, validated_data):
        instance.title = validated_data.pop('title', instance.title)
        
        #Update the relevant answers
        answers_data = validated_data.pop('answers', [])
        instance.answers.all().delete() #Deleting eisting answers
        for answer in answers_data:
            Answer.objects.create(question = instance, **answer)

        instance.save()
        return instance