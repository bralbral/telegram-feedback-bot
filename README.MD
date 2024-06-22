# telegram-feedback-bot

<p>
<a href="https://artifacthub.io/packages/helm/telegram-feedback-bot/telegram-feedback-bot"><img alt="telegram-feedback-bot" src="https://img.shields.io/badge/Helm-0F1689?style=for-the-badge&logo=Helm&labelColor=0F1689"></a>
<a href="https://hub.docker.com/r/bral1488/telegram-feedback-bot"><img alt="telegram-feedback-bot" src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"></a>
</p>


Simple telegram-feedback bot based on [aiogram](https://github.com/aiogram/aiogram) and [sulguk](https://github.com/Tishka17/sulguk).

Use this bot for communicate with users in case you do not want to provide your personal contacts. 

> For example: you are administrator of telegram group or technical support provider.

## Available commands

| Command |    Description    |
|:-------:|:-----------------:|
|  /help  | Show help message |

## Usage

Messages with an **available content type** *(TEXT, ANIMATION, AUDIO, DOCUMENT, PHOTO, VIDEO, VOICE)* will be transferred to **admin group** or **admin chat**.

*(See variable `chat_id` from [config.yaml](deploy/docker/example.config.yaml#L6))*

If the transfer is successful, the requesting party will be notified.

**Admin** can **answer** to message **by reply**. The answer will be sent to the person who asked.

The user will receive the reply as a **reply** to the original message. If the message does not exist, the user will receive a response with a **separate message**.

If the transfer is successful, the administrator will be notified.

You can [customize the bot's responses](deploy/docker/example.config.yaml#12), or use default values.

## Deploy

### Install from source

> Tested on Ubuntu 22.04, python 3.11

Just copy source code:

`git clone https://github.com/bralbral/telegram-feedback-bot.git`

Install requirements:

`pip install -r requirements.txt`

Fill [config.yml](deploy/docker/example.config.yaml) and place it to root dir. (In parent dir to `src`)

Run:

`python3 -m src`

### Install with Docker

> Stable release with `main` tag on [dockerhub](https://hub.docker.com/r/bral1488/telegram-feedback-bot/tags)

Just copy [docker-compose.yml](deploy/docker/example.docker-compose.yml) and fill in  [config.yaml](deploy/docker/example.config.yaml).

Run containers:

`docker-compose up -d` or if you have new docker `docker compose up -d`

Of course, you can build image yourself:

Just copy source code:

`git clone https://github.com/bralbral/telegram-feedback-bot.git`

and build docker image:

`docker build -t <your_image_name>:<your_tag_name>`

### Install with k8s

> Stable release with `main` tag on [dockerhub](https://hub.docker.com/r/bral1488/telegram-youtube-notifier/tags)

Manifests located in [k8s](deploy%2Fk8s) directory.

It consists of `Namespace`, `ConfigMap`, and `Deployment` files.

You need fill sections in  [01_configmap.yaml](deploy%2Fk8s%2F01_configmap.yaml) file.

Apply deployment:

`kubectl apply -f <directory with configs>`

Or you can do it step by step:

`kubectl apply -f <file from config dir>`

#### Install with Helm Chart

[Helm repo](https://artifacthub.io/packages/helm/telegram-feedback-bot/telegram-feedback-bot)

Add repo:

`helm repo add telegram-feedback-bot https://bralbral.github.io/helm/releases/telegram-feedback-bot`

Install chart:

`helm install my-telegram-feedback-bot telegram-feedback-bot/telegram-feedback-bot --version 0.1.0`



## Hosting
You can rent a server from various hosters, for example from [Aeza](https://aeza.net/?ref=380831).

>*By registering via the [link](https://aeza.net/?ref=380831) you will support the project and receive a 15% bonus on your balance, which will be valid for 24 hours.*

The bot will require the simplest VDS, in rubles this is approximately 100-200 for promotional offers, or about 500 rubles per month.

## Develop and Contribute

Feel free to create issue or pull request.

For development, you should install the requirements from [requirements_dev.txt](./requirements_dev.txt)

`pip install -r requirements_dev.txt`

Use [pre-commit.sh](./pre-commit.sh) before commit.

---
### Donations

If you would like to make a donation, you can use the following wallets:

- **USDT(TRC20):** TCDgNR9eXJr5ds8ttEKCteaZKyqX6KthJN
- **USDT(TON):** UQCFEQGkaAzZPNfKEFn4ENfvCMLR2w_04TB16NrkaaDBRudu
- **TON:** UQCFEQGkaAzZPNfKEFn4ENfvCMLR2w_04TB16NrkaaDBRudu

Thank you for considering supporting my work! Your contributions are greatly appreciated and help me continue to improve this project.