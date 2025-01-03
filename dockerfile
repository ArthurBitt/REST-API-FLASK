FROM python:3.10-alpine

WORKDIR /app

FROM python:3.10-slim

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

COPY . .


EXPOSE 5000

CMD ["python", "app.py"]