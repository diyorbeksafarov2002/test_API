from rest_framework.serializers import ModelSerializer
from .models import SectionModels, QuestionModels

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = QuestionModels
        fields = "__all__"


class SectionSerializer(ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = SectionModels
        fields = "__all__"