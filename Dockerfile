# Use the official Python image as a base image
FROM python:3.7

# Set the working directory in the container
WORKDIR /

# Copy the requirements file into the container at /requirements.txt
COPY requirements.txt /requirements.txt

# Install dependencies
RUN pip install -r /requirements.txt

# Copy the entire project directory into the container at /app
COPY ./app /app

# Set the working directory to /app
WORKDIR /app

# Command to run the FastAPI application within the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]