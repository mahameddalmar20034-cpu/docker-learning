# FROM python:3.9

FROM python:3.11-alpine

WORKDIR /usr/src/app

COPY . .
RUN pip install flask redis



EXPOSE 5000

CMD ["python", "app.py"]