from django.http import HttpResponse
from ..models import Bucket
from ..serializers import BucketSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import  status

@api_view(['POST'])
def add_bucket(request):
    if request.method == 'POST':
        data = request.data
        serializer = BucketSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)