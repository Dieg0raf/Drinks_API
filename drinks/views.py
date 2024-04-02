from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Drink
from .serializers import DrinkSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def ListDrinks(request):
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    print(serializer)
    return Response(serializer.data, status=status.HTTP_200_OK)


@login_required
@api_view(['POST'])
def CreateDrink(request):
    print(request.data)
    serializer = DrinkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@login_required
@api_view(['DELETE'])
def DeleteDrink(request, pk):
    try:
        drink = Drink.objects.get(pk=pk) 
    except Drink.DoesNotExist:
        return Response(request.data, status=status.HTTP_404_NOT_FOUND)

    drink.delete()
    return Response(status=202)

@login_required
@api_view(['PATCH'])
def UpdateDrink(request, pk):
    try:
        drink = Drink.objects.get(pk=pk) 
    except Drink.DoesNotExist:
        return Response(request.data, status=status.HTTP_404_NOT_FOUND)

    serializer = DrinkSerializer(drink, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


