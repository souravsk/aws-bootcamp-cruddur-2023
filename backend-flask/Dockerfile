FROM 682666208032.dkr.ecr.ap-south-1.amazonaws.com/cruddur-python:3.10-slim-buster

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

#ENV FLASK_DEBUG=1

EXPOSE ${PORT}

ENV PYTHONUNBUFFERED=1

CMD [ "python3", "-m" ,"-u", "flask", "run", "--host=0.0.0.0", "--port=4567", "--debug"]