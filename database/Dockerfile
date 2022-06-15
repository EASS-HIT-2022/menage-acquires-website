FROM python:3.7
COPY . /database
WORKDIR /database
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 27017
COPY . .
CMD ["python3", "database.py"]