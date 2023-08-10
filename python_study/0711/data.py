import time
import random
random.seed(123)

mypick=list(map(int,input("숫자 6개를 입력하세요").split()))

mypick.sort()

lotto=[]
bonus_num=0

lotto=random.sample(range(1,46),6)

while True:
	bonus_num=random.randint(1,46)
	if bonus_num not in lotto:
		break



lotto.sort()

count=0

print(lotto,"이번주 로또번호 ")
print(bonus_num)

for i in mypick:
	if i in lotto:
		count+=1

bc=True
if bonus_num not in mypick:
	bc=False

print(mypick)



if count==6:
	print("1등")
elif count==5 and bc==True:
	print("2등")
elif count>=5:
	print("3등")
else:
	print("꽝")

