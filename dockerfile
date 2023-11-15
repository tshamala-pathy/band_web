# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

#ADD . /app

# Copy the requirements.txt file into the container
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .


# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
