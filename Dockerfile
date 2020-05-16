FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential
COPY . /
WORKDIR/
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["python', "setup_database.py"]

