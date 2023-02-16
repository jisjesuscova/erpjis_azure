#!/bin/bash

# Update the package list
apt-get update

# Install wkhtmltopdf
apt-get install -y wkhtmltopdf

# Configure wkhtmltopdf path
export WKHTMLTOPDF_PATH=/usr/bin/wkhtmltopdf

# Start the application
gunicorn app:app