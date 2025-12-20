FROM python:3.11-slim

# Install packages required for building wheels (if any)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app .

# Use gunicorn for production-like serving
CMD ["uvicorn", "--host",  "0.0.0.0", "main:app", "--port", "8000"]
