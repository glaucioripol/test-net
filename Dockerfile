# Use the official Python image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Pipfile and Pipfile.lock into the container
COPY Pipfile Pipfile.lock /app/

# Install pipenv and dependencies
RUN pip install pipenv && pipenv install --deploy --system

# Copy the application code into the container
COPY . /app

# Run the command every 3 minutes
CMD sh -c "while true; do pipenv run speed_test; sleep 180; done"
