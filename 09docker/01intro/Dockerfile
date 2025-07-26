# base
FROM python:3.12

#workdir
WORKDIR /app

#copy
COPY . /app

#run
RUN pip install -r requirements.txt

#expose
EXPOSE 5000

#command
CMD ["python", "./app.py"]