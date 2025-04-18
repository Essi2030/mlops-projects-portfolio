
# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy required files
COPY requirements.txt .
COPY iris_model.joblib .
COPY class_names.txt .
COPY api/ ./api/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Start FastAPI app
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
