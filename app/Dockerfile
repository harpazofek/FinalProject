FROM python:alpine3.18
COPY ./req*.txt /app/req*.txt
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r req*.txt   # -vvv
COPY . .
EXPOSE 5005
ENTRYPOINT [ "python", "main.py" ]