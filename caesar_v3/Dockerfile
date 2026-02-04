# CAESAR Backend Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY vessel.py .
COPY monitor.py .
COPY ice_protocol.py .
COPY ice_bridge.py .
COPY dream.py .
COPY GEOMETRY.md .

# Initialize vessel state
RUN python vessel.py

# Expose port (optional, for future API)
EXPOSE 8000

# Default command (can be overridden)
CMD ["python", "ice_bridge.py"]
