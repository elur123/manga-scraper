# Use official lightweight Python image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install dependencies (no cache to reduce image size)
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
