
from django.contrib import admin
from django.urls import path
from myweb import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # 요청이 왔을때 views 모듈의 index 함수가 처리 
    path('django explain/',views.index),
    path('hello/',views.hello),
    path('data/',views.find),
    path("data/detail/<str:itemid>",views.detail),

]
