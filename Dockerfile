FROM python:3.11-slim-bullseye

# Update the package list and install required packages
RUN apt-get update && \
    apt-get install -y git ffmpeg sqlite3 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Copy the application source code to the container and set the working directory
COPY ./requirements.txt /app/requirements.txt

# copy src
COPY ./src /app/src

WORKDIR /app

# Install Python dependencies
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Set the user to non-root
USER 1000