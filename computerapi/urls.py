from django.urls import path
from .views import read_all_bucket, add_bucket

urlpatterns = [
    path('api/v.1/allbuckets', read_all_bucket, name ='read_all_buckets'),
    path('api/v.1/addbucket/', add_bucket, name ='add_bucket'),
]
