#use python as base image
FROM python:3.9-slim

#set the working dir in container
WORKDIR /app

#copy requirements file to working dir
COPY requirements.txt .

#install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#copy all files to working dir
COPY . .

#expose port
EXPOSE 80

#run api service
CMD ["uvicorn", "main.py"]


