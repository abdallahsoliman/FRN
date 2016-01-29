FROM python:onbuild
MAINTAINER Abdallah Soliman


CMD ["gunicorn", "--workers=4", "wsgi", "-b", ":80"]
