from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import QuestionModels, SectionModels
from .serializers import SectionSerializer, QuestionSerializer
@api_view(['GET', 'POST'])
def SectionListCreate(request):
    if request.method == 'GET':
        queryset = SectionModels.objects.all()
        serializer = SectionSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = SectionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def QuestionListCreate(request):
    if request.method == 'GET':
        queryset = QuestionModels.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = QuestionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def CheckQuestionListCreate(request, id, answer):
    try:
        user = get_object_or_404(QuestionModels, id=id)
    except QuestionModels.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = QuestionSerializer(user)
        print(serializer.data)
        if serializer.data["a"].lower() == answer.lower():

            return JsonResponse({
                "correct": True,
            }, status=200)
        else:
            return JsonResponse({
                "correct": False,
            }, status=200)