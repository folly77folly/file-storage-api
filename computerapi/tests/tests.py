from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Bucket
import json
from ..views import edit_bucket

class BucketTests(APITestCase):
    def test_create_bucket(self):
        """
        Ensure we can create a new account bucket.
        """
        #building the url and data to be inserted
        url = reverse('add_bucket')
        data = {'name': 'bucket101'}

        #creating a response object from query
        response = self.client.post(url, data, format='json')

        #checking all resonse codes and values
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bucket.objects.count(), 1)
        self.assertEqual(Bucket.objects.get().name, 'bucket101')


class ViewEditDeleteBucketTests(APITestCase):
    
    def setUp(self):
        """
        Ensuring the setup can add a bucket to test db.
        """
        url = reverse('add_bucket')
        data = {'name': 'bucket101'}

        self.client.post(url, data, format='json')


    def tearDown(self):
        """
        Ensuring the records are deleted after every test case.
        """

        Bucket.objects.all().delete()


    def test_view_bucket(self):
        """
        Ensure we can view the sent bucket name.
        """

        url = reverse('read_all_buckets')

        #getting the posted data
        response = self.client.get(url)

        # to check for both status and the record inserted
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'bucket101') 


    def test_edit_bucket(self):

        bucketlist = Bucket.objects.get()

        #building the url for edit route with the id of bucket
        url = reverse('edit_bucket', args = (bucketlist.id,) )
        data = {'name': 'bucket102'}

        #updating the url with the PUT Method
        response = self.client.put(url, data, format='json')

        # to check for both status and the record inserted
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'bucket102')
    

    def test_delete_bucket(self):
        #get the record to be deleted
        bucketlist = Bucket.objects.get()
        bucket_id = bucketlist.id

        #building the url to be deleted
        url = reverse('remove_bucket', args = (bucketlist.id,))

        response = self.client.delete(url)

        #check if record has been removed
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)