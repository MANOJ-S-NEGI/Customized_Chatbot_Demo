# Use a Python 3.9 base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/requirements.txt

# Install the required dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the entire application directory into the container
COPY . /code

# Copy the en_core_web_sm-2.3.1.tar.gz file into the container
COPY en_core_web_sm-2.3.1.tar.gz /code/en_core_web_sm-2.3.1.tar.gz

# Install the en_core_web_sm-2.3.1.tar.gz file
RUN pip install en_core_web_sm-2.3.1.tar.gz

# Expose port 7860
EXPOSE 7860

# Define the command to run your application (without Uvicorn)
CMD ["python", "app.py"]
