FROM python:3.10
COPY . /backend
WORKDIR /backend
RUN pip3 install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
