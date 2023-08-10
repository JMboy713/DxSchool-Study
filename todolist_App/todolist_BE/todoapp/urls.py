from django.urls import path
from .views import TodoView


urlpatterns=[
    path("todo",TodoView.as_view()), # api/hello 요청이 오면 helloAPI의 함수로 처리.
]