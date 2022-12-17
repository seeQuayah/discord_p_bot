FROM python:3

# Create a new directory for the Python script
RUN mkdir -p /app
WORKDIR /app

# Install the required Python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Python script to the container
COPY script.py .
COPY .env .
# Run the Python script
CMD ["python", "bot.py"]
