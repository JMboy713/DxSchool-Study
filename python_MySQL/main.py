import pymysql
import sys



try:
	# 데이터베이스 연결 객체 생성
	con=pymysql.connect(host='localhost',port=3306,db='player',user='root',passwd='wlals98',charset='utf8')
	# sql 실행 객체 생성
	cursor=con.cursor()
	# 삽입할 이미지 파일의 내용 읽기
	# f=open('dev_hee.PNG','rb')
	# pyt=f.read()
	# f.close()

	# # 데이터 삽입
	# cursor.execute("INSERT INTO BLOBTABLE VALUES(%s,%s)",("devhee.Png",pyt))
	
	
	# 데이터 읽어오기
	cursor.execute("SELECT * FROM BLOBTABLE")
	data=cursor.fetchone()
	# 두번째 데이터가 blob이므로 두번째 데이터를 파일로 변경. 
	print(data[0])
	# 파일을 쓰기모들고 
	f=open(data[0],'wb')
	# 읽은 데이터를 파일에 기록. 
	f.write(data[1])
	f.close()

	con.commit()

except :
	print("예외발생",sys.exc_info())
finally:
	con.close()
