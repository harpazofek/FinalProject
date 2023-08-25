FROM python:3.10.11-alpine3.17
WORKDIR /ansible
COPY req*.txt .
RUN pip install -r req*.txt
COPY . .
CMD ["ansible", "--version"]