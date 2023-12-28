FROM python:3.9
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libgtk-3-0 \
    libnotify-bin \
    libdbus-1-dev \
    libdbus-glib-1-dev \
    x11-apps
RUN pip install pygobject
COPY popup.py /app/popup.py
ENTRYPOINT ["python", "/app/popup.py"]
