FROM python:alpine3.18
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt   # -vvv
COPY . .
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]


