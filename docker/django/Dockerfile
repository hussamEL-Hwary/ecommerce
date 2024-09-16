# Use an official Python runtime as a base image stage one
FROM python:3.8-slim-bullseye as base

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# ENV DEBUG=False
# ENV DATABASE_URL=postgres://azka_vision:azka_vision@postgres:5432/azka_vision

# Secret Key
# https://www.miniwebtool.com/django-secret-key-generator/
ENV DJANGO_SECRET_KEY za3)tv#(z79o=6h16@ig6b1*p4%ksf#2da%n3#3=-t0p6p7w0x

# Install some useful packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Common deps
    git bash curl g++\
    # OpenCV deps
    libglib2.0-0 libsm6 libxext6 libxrender1 \
    # Postgresql
    libpq-dev python3-dev \
    # editors
    nano && \
    apt-get autoremove -y && apt-get clean && \
    rm -rf /var/cache/apt/* /var/lib/apt/lists/* \



# built stage as final
FROM base as final

# Create workdirectory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./requirements.txt .

# Install python dependencies
RUN pip install --no-cache-dir --upgrade pip==23.3.2
RUN pip install --no-cache-dir -r requirements.txt

COPY ./docker/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//g' /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copy the current directory contents into the container at /app
COPY ./ /app

CMD ["/entrypoint.sh"]
