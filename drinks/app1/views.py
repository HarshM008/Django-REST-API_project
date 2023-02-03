from django.http import JsonResponse
from .serializers import DrinkSerializers
from .models import drinks
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'] )
def drink_list(request):

    if request.method == 'GET':
        All_drinks = drinks.objects.all()
        serializer = DrinkSerializers(All_drinks, many = True)
        return Response(serializer.data)
        

    if request.method == 'POST':
        serializer = DrinkSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'] )
def drink_detail(request,id):

    try:
        Drinks = drinks.objects.get(pk=id)
    except drinks.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializers(Drinks)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DrinkSerializers(Drinks, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        Drinks.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
