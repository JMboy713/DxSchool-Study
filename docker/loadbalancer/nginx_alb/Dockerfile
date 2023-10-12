FROM nginx:latest
# 기본 환경설정 제거. 
RUN rm /etc/nginx/conf.d/default.conf
# 환경 설정 파일을 복사
COPY nginx.conf /etc/nginx/conf.d/default.conf

