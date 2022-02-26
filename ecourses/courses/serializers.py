from rest_framework.serializers import ModelSerializer
from .models import MultipleChoice, Answer


class AnswerSeralizers(ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id","name"]

class MultipleChoiceSerializers(ModelSerializer):
    answers   = AnswerSeralizers(many=True)
    class Meta:
        model = MultipleChoice
        fields = ["id","content","correctAnswer","answers"]