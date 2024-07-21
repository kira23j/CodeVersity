FROM python:3.8.13-slim

WORKDIR app

COPY . /app

# Install application dependencies
RUN pip install -r requirements.txt

# Install additional packages for the Docker environment (optional)
RUN pip install this

# (Optional) Command to start your FastAPI application
CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "8000"]
