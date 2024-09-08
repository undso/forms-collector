FROM python:3.12-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY linear-element-434220-j7-c6080403ae41.json .

#CMD [ "python", "./main.py" ]
CMD [ "flask", "--app", "main", "run" ]