FROM python:3.8.10
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./src ./src
CMD ["python", "./src/app.py"]
