#!/usr/bin/env bash
# Setting up servers with web static files

if ! dpkg -l | grep -q nginx; then
	sudo apt-get update
	sudo apt-get install nginx -y
fi

sudo mkdir -p '/data/web_static/releases/test/'
sudo mkdir -p '/data/web_static/shared/'

echo "<h1>Index Test</h1>" | sudo tee '/data/web_static/releases/test/index.html' > /dev/null
sudo ln -sf '/data/web_static/releases/test/' '/data/web_static/current'
sudo chown -R ubuntu:ubuntu '/data/'

printf "server {
	listen 80 default_server;
	listen [::]:80 default_server;

	location /hbnb_static {
		alias /data/web_static/current/;
		index index.html;
	}
}
" | sudo tee "/etc/nginx/sites-available/default" > /dev/null
sudo service nginx restart
