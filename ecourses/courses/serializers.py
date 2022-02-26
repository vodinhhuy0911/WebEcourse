from rest_framework.serializers import ModelSerializer
from .models import MultipleChoice

class MultipleChoiceSerializers(ModelSerializer):
    class Meta:
        model = MultipleChoice
        fields = ["id","content","correctAnswer"]

