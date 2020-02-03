from django.shortcuts import render
from ..models import Bucket
from ..serializers import BucketSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


@api_view(['GET'])
def read_all_bucket(request):

    #query for all objects of Bucket
    all_buckets = Bucket.objects.all()

    #using serilizers to change Bucket model to json
    serializer = BucketSerializer(all_buckets, many = True)

    return Response(serializer.data, status = status.HTTP_200_OK)
