FROM python:3.11-bookworm
RUN apt update && apt install \
    sqlite3

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install 'fastapi[standard]'
COPY ./src /src
RUN mkdir /sqlite
ENTRYPOINT [ "fastapi", "run", "src/main.py" ]