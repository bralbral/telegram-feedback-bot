# telegram-feedback-bot

Simple telegram-feedback bot based on aiogram.

Use this bot for communicate with users in case do not want to provide your personal contacts. 

> For example: you are administrator of telegram group or technical support provider.

## Deploy

### Install from source

> Tested on Ubuntu 22.04, python 3.11

Just copy source code:

`git pull https://github.com/bralbral/telegram-feedback-bot`

Install requirements:

`pip intall -r requirements.txt`

Fill [config.yml](./deploy/example.config.yaml) and place it to root dir. (In parent dir to `src`)

Run:

`python3 -m src`

### Install with Docker

Just copy [docker-compose.yml](./deploy/example.docker-compose.yml) and fill in  [config.yaml](./deploy/example.config.yaml).

Run containers:

`docker-compose up -d` or if you have new docker `docker compose up -d`

Of course, you can build image yourself:

Just copy source code:

`git pull https://github.com/bralbral/telegram-feedback-bot`

and build docker image:

`docker build -t <your_image_name>:<your_tag_name>`

And use this image with [docker-compose.yml](./deploy/example.docker-compose.yml) from `deploy` dir.