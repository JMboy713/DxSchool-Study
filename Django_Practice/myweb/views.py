from django.shortcuts import render
from django.http import HttpResponse
from myweb.models import ITEM



# Create your views here.
def index(request):
    # html을 직접 작성해서 출력
    # return HttpResponse("<h1>Hello Django<h1>")
    msg="안녕하세요"
    person={"name":"jason","age":26}
    data=['stack','queue','Deque','LinkedList','Tree']
	# html 파일을 출력
    return render(request,'index.html',{"msg":msg,"person":person,"data":data})




def hello(request):
    return HttpResponse("<p>say hello<p>")


def find(request):
    data= ITEM.objects.all()
    data1=ITEM.objects.get(itemid='1')
    print(data1)
    return render(request,'index.html',{'data':data})     

def detail(request,itemid):
    item=ITEM.objects.get(itemid=itemid)
    return render(request,'detail.html',{"item":item})