# telegram-feedback-bot

Simple telegram-feedback bot based on [aiogram](https://github.com/aiogram/aiogram) and [sulguk](https://github.com/Tishka17/sulguk).

Use this bot for communicate with users in case you do not want to provide your personal contacts. 

> For example: you are administrator of telegram group or technical support provider.

## Available commands

| Command |    Description    |
|:-------:|:-----------------:|
|  /help  | Show help message |

## Usage

Messages with an available [content type](./src/bot/handlers/users.py#L19) will be transfered to admin group or admin chat.

*(See variable `chat_id` from [config.yaml](./deploy/example.config.yaml#L6))*

If the transfer is successful, the requesting party will be notified.

Admin can answer to message by reply. The answer will be sent to the person who asked.

If the transfer is successful, the administrator will be notified.

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

## Develop and Contribute

Feel free to create issue or pull request.

For development, you should install the requirements from [requirements_dev.txt](./requirements_dev.txt)

`pip intall -r requirements_dev.txt`

Use [pre-commit.sh](./pre-commit.sh) before commit.
