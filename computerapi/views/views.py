from django.shortcuts import render
from ..models import Bucket
from ..serializers import BucketSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# Create your views here
# @api_view(['POST'])
# # @csrf_exempt
# def add_bucket(request):
#     if request.method == 'POST':
#         data = request.data
#         serializer = BucketSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def read_all_bucket(request):
    if request.method == 'GET':
        all_buckets = Bucket.objects.all()
        serializer = BucketSerializer(all_buckets, many = True)
        return Response(serializer.data)
