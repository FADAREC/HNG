# Use an official PHP runtime as a parent image
FROM php:8.0-apache

# Set the working directory in the container
WORKDIR /var/www/html

# Copy the current directory contents into the container at /var/www/html
COPY . .

# Expose port 80 to the outside world
EXPOSE 80

# Set the entry point to Apache to serve the PHP file
CMD ["apache2-foreground"]