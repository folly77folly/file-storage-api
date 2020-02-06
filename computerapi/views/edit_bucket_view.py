from django.http import HttpResponse
from ..models import Bucket
from ..serializers import BucketSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import  status


class BucketDetail(APIView):
    """
    Retrieve, update or delete a bucket instance.
    """
    def get_object(self, bucket_id):

        try:
            return Bucket.objects.get(pk = bucket_id)

        except Bucket.DoesNotExist:

            return Response(status = status.HTTP_400_BAD_REQUEST)

    def get(self, request, bucket_id, format='json'):

        # using request .data because its an API not form
        bucket_detail = self.get_object(bucket_id)

        #serializer object for edit created
        serializers = BucketSerializer(bucket_detail)

        return Response(serializers.data, status = status.HTTP_200_OK)



    def put(self, request, bucket_id, format='json'):

        # using request .data because its an API not form
        data = request.data

        bucket_detail = self.get_object(bucket_id)

        #serializer object for edit created
        serializers = BucketSerializer(bucket_detail, data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status = status.HTTP_200_OK)

        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)


    def delete(self, request, bucket_id, format = 'json'):
        bucket_to_delete = self.get_object(bucket_id)

        #perform delete on a bucket object
        bucket_to_delete.delete()

        return HttpResponse(status = status.HTTP_204_NO_CONTENT)
                