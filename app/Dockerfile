FROM python:3.8-slim
WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:/app"
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3","sleepyBot.py"]