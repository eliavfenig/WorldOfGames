FROM python:3.9-slim
RUN pip install flask
WORKDIR /app
COPY Score /app
CMD ["python", "MainScores.py"]
