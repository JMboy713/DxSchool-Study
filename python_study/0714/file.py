import csv
data=[]
with open('./0714/test.csv','wb') as file:
	file.write("안녕".encode())

with open('./0714/test.csv','rb+') as file:
	content=file.read()
	print(content.decode())

