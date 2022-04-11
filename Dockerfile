FROM python:3.7-alpine
WORKDIR /myapp
COPY . /myapp
RUN pip install -U -r requirements.txt
EXPOSE 80
CMD ["python" , "app2.py"]
