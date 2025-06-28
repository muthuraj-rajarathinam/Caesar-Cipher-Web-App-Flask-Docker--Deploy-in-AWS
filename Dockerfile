# Use the official lightweight Python image
FROM python:3.11-slim

# Set working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy application code
COPY app.py .

# Expose port 5000 for Flask
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
