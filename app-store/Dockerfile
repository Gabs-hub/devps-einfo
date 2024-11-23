FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY app.py requirements.txt index.html ./

# Install dependencies
RUN pip install -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
