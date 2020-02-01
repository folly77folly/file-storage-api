from django.http import HttpResponse
from ..models import Bucket
from ..serializers import BucketSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import  status

@api_view(['DELETE'])
def remove_bucket(request, bucket_id):
    #get the bukcet to edit
    try:
        bucket_to_delete = Bucket.objects.get(pk = bucket_id)
    except Bucket.DoesNotExist:
        return Response(status=404)
    bucket_to_delete.delete()
    return HttpResponse(status = 204)
    