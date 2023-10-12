FROM python:3.11-alpine 
# 캐시를 지우고 bash 에 접속.
RUN apk update && apk add --no-cache bash
# python 관련 라이브러리 업데이트
RUN apk --update add python3 py3-pip python3-dev

# 환경 설정
ENV LIBRARY_PATH=/lib:/usr/lib
ENV FLASK_APP=py_app
ENV FLASK_ENV=development

EXPOSE 9000
WORKDIR /py_app
COPY . .

RUN pip install -r requirements.txt

# 컨테이너로 만들어 질 때 실행할 명령어
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]

