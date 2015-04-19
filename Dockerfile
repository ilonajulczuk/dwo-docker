# let's start from the image with python installed
FROM python:3.4

# Add file with dependencies to the container
ADD requirements.txt /code/requirements.txt

# Run a command inside a container
RUN pip install -r /code/requirements.txt

# set working diretory
WORKDIR /code

# copy code from current directory to /code
COPY . /code

# expose port from container
EXPOSE 5000

# default command that will be run in container
CMD python app.py
