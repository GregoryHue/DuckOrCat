FROM tensorflow/tensorflow:latest-gpu
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["gunicorn", "-w", "4", "-b",  "0.0.0.0", "main:app"]
