FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (including supervisor)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application code
COPY . .

# Expose ports for both (FastAPI: 8000, Streamlit: 8501)
EXPOSE 8000
EXPOSE 8501

# Supervisor configuration to manage both processes simultaneously
COPY supervisord.conf /etc/supervisor/supervisord.conf

# Start supervisor to keep both services running as one single AWS unit
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
