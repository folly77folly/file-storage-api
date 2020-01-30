from django.http import HttpResponse
from ..models import Bucket
from ..serializers import BucketSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import  status

@api_view(['PUT'])
def edit_bucket(request, bucket_id):
    #get the bukcet to edit
    try:
        bucket_to_edit = Bucket.objects.get(pk = bucket_id)
    except Bucket.DoesNotExist:
        return Response(status=404)
    data = request.data
    serializers = BucketSerializer(bucket_to_edit, data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status = status.HTTP_200_OK)
    return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)