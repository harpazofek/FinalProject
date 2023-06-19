FROM python:alpine3.18
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5000
ENTRYPOINT ["main.py"]
# CMD flask run -h 0.0.0.0 -p 5000


# CMD [ "flask", "run" ]
# ENTRYPOINT [ “python” ]
# CMD [ “main.py” ]

# FROM ubuntu
# RUN apt update
# RUN apt install python3-pip -y
# RUN pip3 install flask
