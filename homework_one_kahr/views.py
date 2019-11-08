from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers


@api_view(['GET', 'POST'])
def animal_list(request):
    if request.method == 'GET':
        animal = models.Animal.objects.all()
        serializer = serializers.AnimalSerializer(animal, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def animal_detail(request, pk):
    try:
        animal = models.Animal.objects.get(pk=pk)
    except models.Animal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.AnimalSerializer(animal)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.AnimalSerializer(animal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        animal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
