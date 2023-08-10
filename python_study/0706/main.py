def outer():
	def inner():
		print("내부함수")
	return inner
# 함수를 호출해서 그 결과를 변수에 대입하고 그 변수를 통해서 함수를 호출한다. 

func=outer()
func() # inner 출력

# a=lambda x,y:x+y
# a(1,2)