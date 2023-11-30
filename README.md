# django-docker-example

Simple project which shows how to create a simple webapp on linux and run it with dockerize it in the end.

Livesteam (German): <https://www.youtube.com/watch?v=MNQjEDvu_iw>

## Run finished product in docker

```bash
bash run_docker.sh
```

### (Access sh in docker)

```bash
docker exec -it CONTAINERID sh -l
```

## Dev setup

```bash
sudo apt install python3-venv python3-dev python3-pip
python3 -m venv .env
source .env/bin/activate
pip install django
cd demochecklist
python manage.py migrate
python manage.py runserver
```
