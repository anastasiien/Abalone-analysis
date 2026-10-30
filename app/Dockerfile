FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY dataset.csv dashboard.py app.py ./

# обучаем модель и сохраняем дашборд при сборке образа
RUN python dashboard.py

EXPOSE 9050
CMD ["python", "app.py"]
