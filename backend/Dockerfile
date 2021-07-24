FROM python:3.9

ADD ./backend /app
RUN pip install -r /app/requirements.txt
WORKDIR /app
ENTRYPOINT python /app/main.py
