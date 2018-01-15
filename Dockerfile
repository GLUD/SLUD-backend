FROM python:3-alpine
LABEL maintainer "Sebastian Tabares Amaya <sytabaresa@gmail.com>"

RUN apk --no-cache add postgresql-client nano

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

# Mejor en el CMD (por SECRET_KEY)
#RUN python manage.py migrate
#RUN python manage.py collectstatic

EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["./run.sh"]
