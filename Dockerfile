# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install flask pygal lxml requests

# Expose the port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]