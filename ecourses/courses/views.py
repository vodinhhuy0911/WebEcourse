from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import MultipleChoice
from .serializers import MultipleChoiceSerializers
# Create your views here.

class MultipleChoiceViewSet(viewsets.ModelViewSet):
    queryset = MultipleChoice.objects.all()
    serializer_class = MultipleChoiceSerializers



def index(request):
    return render(request,template_name='index.html',
                  context={ 'name':"Vo Dinh Huy"
    })
