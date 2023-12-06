#!/usr/bin/env bash
# A bash script that prepares my servers for application deployment.

# checking if nginx is installed

check=$(command -v nginx)

if [[ -z "$check" ]]
then
	apt-get -y update
	apt-get -y install nginx
fi

# creating necessary directories and files

if ! [[ -d "/data/" ]]
then
	sudo mkdir /data/
fi

if ! [[ -d "/data/web_static/" ]]
then
	sudo mkdir -p /data/web_static/
fi

if ! [[ -d "/data/web_static/releases/" ]]
then
	sudo mkdir -p /data/web_static/releases/
fi

if ! [[ -d "/data/web_static/shared/" ]]
then
	sudo mkdir -p /data/web_static/shared/
fi

if ! [[ -d "/data/web_static/releases/test/" ]]
then
	sudo mkdir -p /data/web_static/releases/test/
	sudo touch /data/web_static/releases/test/index.html
	echo "<html>
	<head></head>
	<body>
	Holberton School
	</body>
	</html>"  | sudo tee /data/web_static/releases/test/index.html
fi

if [[ -L "/data/web_static/current" ]]
then
	sudo rm /data/web_static/current
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current
else
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current
fi

sudo chown -R ubuntu:ubuntu /data/

# configuring nginx configuration file

serve_me="\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "58i$serve_me" /etc/nginx/sites-available/default
sudo service nginx restart
