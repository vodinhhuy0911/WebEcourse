from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import MultipleChoice,Answer
from .serializers import MultipleChoiceSerializers,AnswerSeralizers
# Create your views here.

class MultipleChoiceViewSet(viewsets.ModelViewSet):
    queryset = MultipleChoice.objects.all()
    serializer_class = MultipleChoiceSerializers

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSeralizers


def index(request):
    return render(request,template_name='index.html',
                  context={ 'name':"Vo Dinh Huy"
    })
