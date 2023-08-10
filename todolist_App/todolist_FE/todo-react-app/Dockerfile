# 노드 설치 
From node:alpine 

#경로 설정
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH

# 설치
COPY package.json /app/package.json
RUN npm install --force	
RUN npm install react-scripts@5.0.1 -g

#포트 설정
EXPOSE 3000

#npm start
CMD ["npm","start"]