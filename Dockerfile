FROM python:3.8

COPY u2net.onnx /home/.u2net/u2net.onxx

WORKDIR /app

COPY dependencies.txt .

RUN pip install --no-cache-dir -r dependencies.txt

COPY . .

EXPOSE 7777

CMD ["python", "app.py"]