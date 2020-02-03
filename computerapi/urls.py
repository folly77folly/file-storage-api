from django.urls import path
from .views import read_all_bucket, add_bucket ,edit_bucket, remove_bucket

urlpatterns = [
    path('api/v.1/allbuckets', read_all_bucket, name ='read_all_buckets'),
    path('api/v.1/editbucket/<int:bucket_id>', edit_bucket, name ='edit_bucket'),
    path('api/v.1/removebucket/<int:bucket_id>', remove_bucket, name ='remove_bucket'),
    path('api/v.1/addbucket/', add_bucket, name ='add_bucket'),
]
