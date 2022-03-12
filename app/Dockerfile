##
# app/Dockerfile

FROM python:3.8-slim-buster

# set the working directory in the container
WORKDIR /app

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "python3", "-u", "./hello.py"]