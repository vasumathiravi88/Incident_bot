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
RUN echo '[supervisord]\nnodaemon=true\n\n[program:api]\ncommand=uvicorn main:app --host 0.0.0.0 --port 8000\nautostart=true\nautorestart=true\n\n[program:streamlit]\ncommand=streamlit run app.py --server.port=8501 --server.address=0.0.0.0\nautostart=true\nautorestart=true' > /etc/supervisor/conf.d/supervisord.conf

# Start supervisor to keep both services running as one single AWS unit
CMD ["/usr/bin/supervisord"]
