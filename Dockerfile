# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container.
WORKDIR /app

# Copy the current directory contents into the container at /app.
COPY . /app

# Install the Python dependencies specified in the requirements file.
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 to allow Streamlit to be accessible.
EXPOSE 8501

# Run Streamlit when the container launches.
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]
