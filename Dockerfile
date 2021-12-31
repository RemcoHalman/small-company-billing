FROM python:alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Running the installation commands
RUN ./manage.py makemigrations
RUN ./manage.py migrate
RUN ./manage.py loaddata fixtures/*