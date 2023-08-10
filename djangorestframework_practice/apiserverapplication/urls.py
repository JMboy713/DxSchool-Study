from django.urls import path
from .views import helloAPI,insertAPI,getoneAPI

urlpatterns=[
    path("hello",helloAPI),
    path("fbv/insert",insertAPI),
    path("fbv/select/<int:bid>",getoneAPI)
]
    