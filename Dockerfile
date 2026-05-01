# Base image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copy files
COPY . .

# Install deps
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 10000

# Run app
CMD ["gunicorn", "-b", "0.0.0.0:10000", "app:app"]
