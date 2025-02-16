# Use a lightweight Python base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install any necessary Python packages
RUN pip install --no-cache-dir kfp datasets

# Copy all necessary files into the container
COPY pipeline.py preprocess.py train.py evaluate.py deploy.py ./
