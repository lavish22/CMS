# Use an official Python runtime as a parent image
FROM python:3.8
LABEL version="1.01"

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=cms.settings.production
#ENV DJANGO_ENV production

COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install -r /code/requirements.txt
RUN pip install gunicorn

# Copy the current directory contents into the container at /code/
COPY . /code/
# Set the working directory to /code/
WORKDIR /code/

RUN python manage.py migrate

#RUN python manage.py collectstatic --no-input

#RUN useradd wagtail
#RUN chown -R wagtail /code
#USER wagtail

EXPOSE 8000
CMD exec gunicorn cms.wsgi:application --bind 0.0.0.0:8000 --workers 2 --threads=4 --worker-class=gthread

#docker container run --publish 8000:8000 --detach <wagtail-cms>
