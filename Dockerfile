# Specify Ubuntu 22.04 as the base image of our Docker container
FROM ubuntu:22.04

# Set a non-interactive frontend for apt (prevents tzdata from prompting)
ENV DEBIAN_FRONTEND=noninteractive

# Update and upgrade packages
RUN apt-get update && apt-get upgrade -y && apt-get install -y wget gnupg2 software-properties-common unzip curl

# Install dependencies for running a headless browser
RUN apt-get install -y xvfb x11-utils

# Add deadsnakes PPA to install Python 3.11
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y python3.11 python3-pip

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install a virtual environment:
RUN pip install virtualenv
RUN virtualenv /opt/venv

# Activate virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Install necessary dependencies for Google Chrome
RUN apt-get install -y wget gnupg ca-certificates

# Add Google Chrome repository key
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Add Google Chrome repository
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list

# Update package lists
RUN apt-get update

# Install Google Chrome
RUN apt-get install -y google-chrome-stable

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# Environment variable to detect Docker
ENV DOCKER_ENV=true 

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run main.py when the container launches
CMD ["gunicorn", "-b", "0.0.0.0:8080", "--timeout", "120", "app:app"]
