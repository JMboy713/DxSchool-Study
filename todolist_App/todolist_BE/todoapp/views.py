from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import View
from .models import Todo
from django.http import JsonResponse # json 응답을 만들기 위한 import 
from rest_framework import status
from .serializers import TodoSerializer
import datetime # 날짜를 사용하기 위한 import 
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



@method_decorator(csrf_exempt,name='dispatch')
# 클래스의 get,post,put,delete 메서드가 각 요청 방식을 처리
class TodoView(View):
	def get(self,request):
		# 파라미터 읽기.
		userid=request.GET.get('userid',None) # 뒤의 none은 userid 가 없다면 none 을 넣기 위해. 
		if userid!=None:
			todos=Todo.objects.filter(userid=userid)
		else:
			todos=Todo.objects.all()
			
		# serializer=TodoSerializer(todos,many=True)
		# return Response(serializer.data,status=status.HTTP_200_OK)
		# json 응담. list 라는 키로 검색된 데이터를 list 로 전달.
		return JsonResponse({'list':list(todos.values())},status=status.HTTP_200_OK)		
    
	def post(self,request):
		params=json.loads(request.body)
		# print(type(params))
		userid=params["userid"]
		title=params["title"]
		
		# 삽입할 객체 생성
		todo=Todo()
		todo.userid=userid
		todo.title=title
		todo.moddate=datetime.datetime.today()
		
		todo.save()
		# 삽입후 결과 처리. 
		# 일반적으로 삽입한 데이터만 리턴하던가, 전체 데이터를 리턴함
		todos=Todo.objects.filter(userid=userid)
		return JsonResponse({'list':list(todos.values())},status=status.HTTP_200_OK)
    
	def put(self,request):
		# 클라이언트의 파라미터 읽기
		params=json.loads(request.body)
		id=params["id"]
		userid=params["userid"]
		title=params["title"]
		done=params["done"]
        
        
		# 서버에서의 처리
		# db 작업 이외의 작업을 한다면 별도의 클래스를 만들어서 처리한 후 리턴을 받아서 다음 작업을 수행한다. 
		# id에 해당하는 데이터를 찾아서 done 의 값을 수정
		todo=Todo.objects.get(id=id)
		todo.done=done
		todo.title=title
		todo.moddate=datetime.datetime.today()
		todo.save()

		# 응답 만들기
		todos=Todo.objects.filter(userid=userid)
		return JsonResponse({'list':list(todos.values())},status=status.HTTP_200_OK)
	
	def delete(self,request):
		params=json.loads(request.body)
		id=params["id"]
		userid=params["userid"]
		
		# 데이터 찾아오기
		todo=Todo.objects.get(id=id)
		todo.delete()
		# 응답 만들기
		todos=Todo.objects.filter(userid=userid)
		return JsonResponse({'list':list(todos.values())},status=status.HTTP_200_OK)