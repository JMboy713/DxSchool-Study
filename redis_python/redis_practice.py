import redis
import time
'''
# 접속 (연결 해제를 하지 않아도 됨) 
with redis.StrictRedis(host="localhost",port=6379) as conn:
    # 문자열 저장
	conn.set("car_name","제네시스")
	conn.set("car_name","sonata")
    # 문자열 가져오기 - bytes 로 return 
	data=conn.get("name")
	print(data)# 인코딩 결과가 출력됨.
	print(data.decode('utf-8')) # b'adam' -> bytes adam 
'''

'''
# connection Pool 을 이용한 접속
redis_poll=redis.ConnectionPool(host='localhost',port=6379,max_connections=4)
with redis.StrictRedis(connection_pool=redis_poll) as conn:
	# 만료시간 설정 가능
	conn.set("company","LG",10)
	# 만료 시간 확인 - TTL
	print(conn.ttl("company"))

	# 이미 만들어진 데이터의 만료시간
	conn.set("song","노래")
	conn.expire("song",10)
	print(conn.get("song"))
	time.sleep(20)
	print(conn.get("song")) # 20초 후에 데이터를 가져오므로 데이터가 없어져서 none을 출력

    # 문자열 저장
	conn.set("car_name","제네시스")
    # 문자열 가져오기 - bytes 로 return 
	data=conn.get("name")
	print(data)# 인코딩 결과가 출력됨.
	print(data.decode('utf-8')) # b'adam' -> bytes adam 
'''
redis_poll=redis.ConnectionPool(host='localhost',port=6379,max_connections=4)
with redis.StrictRedis(connection_pool=redis_poll) as conn:
	# 리스트에 데이터 저장
	conn.lpush("album","genesis")
	conn.rpush("album","exodus")
	for album in conn.lrange("album",0,10):
		print(album)