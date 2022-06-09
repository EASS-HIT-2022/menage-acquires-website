FROM python:3.10

COPY . /frontend

WORKDIR /frontend

RUN pip3 install -r requirements.txt

EXPOSE 8501

CMD ["streamlit","run","ui.py"]