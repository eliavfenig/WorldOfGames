FROM python:3.9-slim
RUN pip install flask
WORKDIR /app
COPY MainScores.py /app
COPY Utils.py /app
COPY scores.txt /app
COPY templates /app
CMD ["python", "MainScores.py"]
