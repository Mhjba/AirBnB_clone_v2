#!/usr/bin/env bash
# Install Nginx if not already installed

if ! cmd -l | grep -q nginx; then
	sudo apt-get update
	sudo apt-get install nginx -y
fi

# Create necessary directories
sudo mkdir -p '/data/web_static/releases/test/'
sudo mkdir -p '/data/web_static/shared/'

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee '/data/web_static/releases/test/index.html' > /dev/null
# Create symbolic link
sudo ln -sf '/data/web_static/releases/test/' '/data/web_static/current'
# Set ownership recursively
sudo chown -R ubuntu:ubuntu '/data/'

# Update Nginx configuration
printf "server {
	listen 80 default_server;
	listen [::]:80 default_server;

	location /hbnb_static {
		alias /data/web_static/current/;
		index index.html;
	}
}
" | sudo tee "/etc/nginx/sites-available/default" > /dev/null
# Restart Nginx
sudo service nginx restart

