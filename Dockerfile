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

# Copy NGINX config and enable it
COPY nginx.conf /etc/nginx/sites-available/default
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

# Copy entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose ports
EXPOSE 80

# Set entrypoint script
ENTRYPOINT ["/entrypoint.sh"]
