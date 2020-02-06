from django.shortcuts import render
from ..models import Bucket
from ..serializers import BucketSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class BucketList(APIView):
    """
    View to list all buckets in the system.
    """

    def get(self, request, format='json'):
        """
        Return a list of all buckets.
        """
        #query for all objects of Bucket
        all_buckets = Bucket.objects.all()

        #using serilizers to change Bucket model to json
        serializer = BucketSerializer(all_buckets, many = True)

        return Response(serializer.data, status = status.HTTP_200_OK)
    


    def post(self, request, format='json'):
        #collecting data from request
        data = request.data

        #using serializer on the Bucket model
        serializer = BucketSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)