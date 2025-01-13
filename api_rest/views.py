from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer
import logging

import json

logging.basicConfig(level=logging.DEBUG)

# Create your views here.

@api_view(['GET'])
def get_users(request):
  if request.method == 'GET':
    users = User.objects.all()
    
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
  return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_by_nick(request, nick):
 
  try:
    user = User.objects.get(pk=nick)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = UserSerializer(user)
    user_data = serializer.data
    
    logging.debug(f'serializer data: {serializer.data}')
    
    if user_data['user_age'] > 18:
      user_data['is_adult'] = True
    else:
      user_data['is_adult'] = False
      
    return Response(user_data)
  
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):
  if request.method == 'GET':
    try:
      if request.GET['user']:
        user_nickname = request.GET['user']
        
        try:
          user = User.objects.get(pk=user_nickname)
        except:
          return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user)
        return Response(serializer.data)
        
      else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    except:
      return Response(status=status.HTTP_404_NOT_FOUND)