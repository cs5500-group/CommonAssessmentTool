# Use Python 3.11 image as base
FROM python:3.11

# Set working directory
WORKDIR /code

# Copy requirements first to leverage Docker cache
COPY ./requirements.txt /code/requirements.txt

# Install required packages
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy the rest of your application
COPY . /code/

# Expose the port your app runs on
EXPOSE 8080

# Command to run the application
CMD ["sh", "-c", "python -m uvicorn app.main:app --host 0.0.0.0 --port=$PORT"]
