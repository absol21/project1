from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from . import serializers

@api_view(['GET'])
def get_person(request):
    all_people = Person.objects.all()
    serializer = serializers.PersonSerializer(all_people, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def detail_person(request, pk):
    try:
        person = Person.objects.get(id = pk)
        serializer = serializers.PersonSerializer(person)
        return Response(serializer.data, status =200)
    except Person.DoesNotExist:
        return Response(f'Person did not found {pk}!', status=404)

@api_view(['POST'])
def create_person(request):
    serializer = serializers.PersonSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)

@api_view(['DELETE'])
def deleat_person(request, pk):
    try:
        person = Person.objects.get(id=pk)
        person.delete()
        return Response('Deleted succesfully', status=204)
    except Person.DoesNotExist:
        return Response(f'Person with key {pk} is not Deleted. Person does not exist', status=404)

@api_view(['PUT', 'PATCH'])
def update_person(request, pk):
    try:
        person=Person.objects.get(id=pk)
        if request.method == 'PUT':
            serializer = serializers.PersonSerializer(instance=person, data=request.data)
        else:
            serializer =serializers.PersonSerializer(instance=person, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=206)
    except Person.DoesNotExist:
        return Response('Does not exist', status=404)
    