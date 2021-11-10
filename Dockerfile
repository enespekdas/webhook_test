FROM python:3.9-slim-buster
WORKDIR /webhook
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD server.py .
EXPOSE 5000
CMD ["python","server.py"]

