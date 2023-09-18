FROM python:3.9-slim

# Set a working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Command to run the script
CMD ["python", "./your_script_name.py"]
