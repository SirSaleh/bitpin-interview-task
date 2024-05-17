FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt /app/

RUN apk update && \
    apk add --no-cache gcc musl-dev linux-headers libffi-dev jpeg-dev zlib-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY bitpin_task /app/bitpin_task

ENV DJANGO_SETTINGS_MODULE=bitpin_task.settings \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

EXPOSE 8000

CMD ["python", "bitpin_task/manage.py", "runserver", "0.0.0.0:8000"]
