FROM python:3.8

WORKDIR /my_toolkit

COPY ./my_toolkit .

RUN pip install -r requirements.txt

CMD ["python", "tell_date.py"]