#!/usr/bin/env bash
# Configures Nginx so that its HTTP response contains a custom header:
# The name of the custom HTTP header must be X-Served-By
# The value of the custom HTTP header must be the hostname of the server Nginx is running on

sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p  /data/web_static/shared/
sudo mkdir -p  /data/web_static/releases/test/

# create placeholder
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# symlink
ln -sf /data/web_static/releases/test/ /data/web_static/current

# change ownership of folder
chown -hR ubuntu:ubuntu /data


sed -i "/server_name _/a location \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}" /etc/nginx/sites-available/default

sudo service nginx restart
