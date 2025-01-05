FROM python:3.10-slim

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libyaml-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools

# Copy and install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install gunicorn
RUN pip install gunicorn

COPY wsgi.py .
COPY config.py .
COPY application application

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "wsgi:app"]