# Dockerfile
# Set base image
FROM python:3.9

MAINTAINER "Dmitry <7292337@gmail.com>"
LABEL version="1.0"
LABEL description="Tree Segmentation FastAPI + Telegram Bot"

# Set the working directory
WORKDIR /app

# Copying the dependencies file
COPY requirements.txt .

# Installing dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copying files into working directory
COPY . .

# Port to be listening at runtime
EXPOSE 8001

# Running the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]
