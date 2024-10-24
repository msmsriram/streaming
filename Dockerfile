# Base image
FROM python:3.12.5-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y tor curl && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Add the FastAPI app code
COPY . /app
WORKDIR /app

# Run Tor as a background service and then start the FastAPI app
CMD ["sh", "-c", "service tor start && uvicorn main:app --host 0.0.0.0 --port 8000"]
