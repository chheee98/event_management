# Base image for Python
FROM python:3.10-slim

# Install required system packages
RUN apt-get update && apt-get install -y nginx && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /event_management_api

# Copy application files
COPY . /event_management_api

# Install Python dependencies
COPY requirements.txt /event_management_api/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set a default SECRET_KEY for the build process
ENV SECRET_KEY="temporary_secret_key"

# Collect static files
RUN python manage.py collectstatic --noinput

# Run database migrations
RUN python manage.py migrate --noinput

# Copy NGINX config and enable it
COPY nginx.conf /etc/nginx/sites-available/default
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

# Expose ports
EXPOSE 80

# Start NGINX and Gunicorn
CMD service nginx start && gunicorn configs.wsgi:application --bind 0.0.0.0:8000 --workers=3
