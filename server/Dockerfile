FROM python:3.11-bookworm
RUN apt update && apt install \
    sqlite3

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./main.py main.py
ENTRYPOINT [ "python3", "main.py" ]