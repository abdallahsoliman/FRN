FROM ubuntu
MAINTAINER Abdallah Soliman
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get -y update
RUN apt-get -y upgrade

# install necessary packages
RUN apt-get -y install dialog vim nginx python3 python3-pip python3-dev python-virtualenv git

# configure git
RUN git config --global user.name "CWRU FRN"
RUN git config --global user.email "frn-exec@case.edu"

# pull latest FRN from git repo
RUN mkdir -p /var/www
RUN git clone https://github.com/abdallahsoliman/FRN.git /var/www/frn

# setup virtualenv & install requirements
RUN cd /var/www/frn && virtualenv -p /usr/bin/python3 venv && source venv/bin/activate && pip install -r requirements.txt && pip install uwsgi


# uWSGI, nginx, flask configuration
RUN rm /etc/nginx/sites-enabled/default
RUN rm /etc/nginx/sites-available/default
ADD wsgi.py /var/www/frn/
ADD frn.ini /var/www/frn/
ADD frn.conf /etc/init/
ADD frn /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/frn /etc/nginx/sites-enabled
RUN service nginx restart
