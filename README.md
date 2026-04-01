```shell
docker run -d --restart unless-stopped --name pinger \
-p 127.0.0.1:32432:8000 -e TZ=Europe/Moscow \
ghcr.io/astral-sh/uv:debian-slim \
uv run --script https://github.com/Albus/prtg-tcpping/raw/refs/heads/master/main.py
```
