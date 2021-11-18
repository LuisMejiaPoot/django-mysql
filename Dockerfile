FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN pip install mysqlclient
RUN pip install python-dotenv
RUN pip install requests
RUN pip install blockcypher