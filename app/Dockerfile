FROM python:3.8-slim

# Set the working directory to /app/src
WORKDIR /src

# Set the PYTHONPATH to include /app/src
ENV PYTHONPATH "${PYTHONPATH}:/app/src"

# Copy the requirements.txt file to /app/src
COPY src/requirements.txt .

# Install the dependencies
RUN pip3 install -r requirements.txt
# Install dependencies for ps command used as container healthcheck
RUN apt-get update && apt-get install -y procps

# Copy the rest of the application code to /app/src
COPY src/ .

# Run the application
CMD ["python3", "sleepyBot.py"]
