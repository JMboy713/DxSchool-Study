FROM python:3
COPY . .
WORKDIR /
RUN pip install flask
COPY . /
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]