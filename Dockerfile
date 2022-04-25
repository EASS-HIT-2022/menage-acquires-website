FROM python:3.10

RUN mkdir /backend

COPY requirements.txt /backend

RUN pip install -r requirements.txt

COPY . /backend 

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
