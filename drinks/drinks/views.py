from .models import Drikns
from django.http import JsonResponse
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        drinks = Drikns.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return  JsonResponse({"drinks":serializer.data}, safe=False)

    if request.method == 'POST':
        drink_serializer = DrinkSerializer(data= request.data)
        if drink_serializer.is_valid():
            drink_serializer.save()
            return Response(drink_serializer.data, status = status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT' , 'DELETE'])

def drink_detail(request , id):  
    try:
        object = Drikns.objects.get(pk=id)
    except Drikns.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)      
    if request.method == 'GET':
        serializer = DrinkSerializer(object)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = DrinkSerializer(object , request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)