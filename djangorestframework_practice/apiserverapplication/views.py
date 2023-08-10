from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Book
from .serializers import BookSerializer


@api_view(['GET']) 
def helloAPI(request):
	return Response("hello world")

@api_view(['GET','POST'])
def insertAPI(request):	
	# GET 방식 처리
	if request.method=='GET':
		books=Book.objects.all()
		serializer=BookSerializer(books,many=True)
		return Response(serializer.data,status=status.HTTP_200_OK)
	
	# POST 방식 처리
	elif request.method=='POST':
		# 클라이언트가 전송한 데이터를 삽입. 
		# 클라이언트가 전송한 데이터를 모델이 사용할 수 있는 데이터로 만든다. 
		serializer=BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


from rest_framework.generics import get_object_or_404	
@api_view(['GET'])
def getoneAPI(request,bid):	
	# 기본키 가지고 데이터 1개 가져오기
	books=get_object_or_404(Book,bid=bid)
	serializer=BookSerializer(books)
	return Response(serializer.data,status=status.HTTP_200_OK)

def ajax(request):
	return render(request,"ajax.html")