import pickle

class DTO:
	def __init__(self,num=0,name="no_name") :
		self.__num=num
		self.__name=name

	@property
	def num(self):
		return self.__num
	@num.setter
	def num(self,num):
		self.__num=num

	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self,name):
		self.__name=name

	# 인스턴스를 print 함수에 대입했을 때 호출되는 메서드
	# 출력을 위해 재정의 - 디버깅 목적. 
	def __str__(self) -> str:
		return str(self.__num) +":"+self.__name


# 파일에 기록할 데이터 생성
dto=DTO(1,"jason")
dto2=DTO(2,"sksksk")
print(dto)
print(dto2)

data=[dto,dto2]



try:
	with open ("./0714/data.data","wb") as f:
		# f에 data를 serializable함. 
		pickle.dump(data,f)
except Exception as e:
	print(e)

try:
	with open ("./0714/data.data","rb") as f:
		# f에 data를 serializable함. 
		result=pickle.load(f)
		for dto in result:
			print(dto)
except Exception as e:
	print(e)