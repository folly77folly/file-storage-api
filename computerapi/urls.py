from django.urls import path
from .views import  BucketList, BucketDetail


urlpatterns = [
    path('api/v.1/allbuckets', BucketList.as_view(), name ='read_all_buckets'),
    path('api/v.1/editbucket/<int:bucket_id>', BucketDetail.as_view(), name ='edit_bucket')
]

