FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY backend/requirements.txt .
RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ .

# Expose port (Railway sets this automatically)
EXPOSE 8000

# Start command
CMD python -m uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}

