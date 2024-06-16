FROM python:3.11-alpine

WORKDIR /app

# Copy the application source code to the container
COPY ./requirements.txt /app/requirements.txt
COPY ./src /app/src

# Update the package list, install required packages, and install Python dependencies
RUN apk update && \
    apk add --no-cache git && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/cache/apk/*

# Set the user to non-root
USER 1000
