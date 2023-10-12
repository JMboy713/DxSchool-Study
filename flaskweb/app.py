import time
import redis
from flask import Flask

app=Flask(__name__)


def web_hit_count():
    # redis 에 접속해서 접속 수 만큼 return .
    with redis.StrictRedis(host='192.168.0.75',port=6379)as conn:
        return conn.incr('hits')


# ip 와 포트번호(도메인) 만 가지고 요청할 떄 . 
@app.route("/")
def func1():
    cnt=web_hit_count()
    return '''
	<h1 style="text-align:center;color:black;">docker-compose application</h1>
    <p style="text-align:center;color:deepskyblue;">web access count:{} times</p>
    '''.format(cnt)

# 어떤 ip를 사용해도 좋고 9000번 포트로 접속해야함. 개발모드로 실행. 
if __name__=="__main__":
    app.run(host='0.0.0.0',port=9000,debug=True) # host에 0.0.0.0 을 넣으면 모든 ip 접속 가능. 