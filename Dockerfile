# Use a Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install the Kubernetes client
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY listpods.py .

# Command to run your script
CMD ["python", "listpods.py"]