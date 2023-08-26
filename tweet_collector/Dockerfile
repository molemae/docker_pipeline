# Use an official Python runtime as base image
FROM  python:3.9

# Set the working directory (app_folder) in the container 
WORKDIR /app

# Copy the requirements and anything else in this folder
COPY . /app

# Install the needed packages specified in the requirements folder
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# What should be executed when the container start:
CMD [ "python","get_mastodon.py" ]