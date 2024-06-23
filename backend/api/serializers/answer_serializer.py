from rest_framework import serializers
from api.models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'question_id',
            'answer_text',
            'is_right'
        ]

