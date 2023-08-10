# mongo db 사용을 위한 패키지 import
from pymongo import MongoClient

conn=MongoClient("localhost",port= 27017)

print(conn)

db=conn.adam # 없다면 생성됨. 

# 컬렉션 설정. 
collect=db.data

# # 데이터 삽입이나 삭제, 갱신을 하게 되면 결과를 return 한다. 
collect.drop()
collect.insert_one({"empno":"10001","name": "김지민","phone":"010-1111-1111","age":26})
result=collect.insert_many([{"empno":"10002","name": "하민수","phone":"011-1111-1111","age":31},
                    {"empno":"10003","name": "김한경","phone":"011-1111-1111","age":50}])

'''
# 데이터 조회
# 데이터 조회를 하게 되면 cursor 를 return 한다. 
# 커서를 순서대로 접근하면 데이터가 dict 로 접근가능하다. 
# cursor 는 앞으로만 전진한다. 끝나고 나면 반복문을 다시 못돌림 .
result=collect.find()
for i in result:
    print(i.get("name","no Name"))
    print(i["name"])

result=collect.find({"age":{"$gt":30}}).sort("age")
for i in result:
    print(i.get("name","no Name"))
    print(i["name"])
''' 

# 수정
collect.update_many(
    {'empno':"10001"},
    {"$set":{'name':"박정헌"}}
)