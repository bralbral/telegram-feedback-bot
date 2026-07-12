FROM python:3.12-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY ./src /app/src
RUN mkdir /app/data && chown 1000:1000 /app/data

# Set the user to non-root
USER 1000

CMD ["python", "-m", "src"]
