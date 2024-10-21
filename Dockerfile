# Используем официальный Python-образ с версией 3.12
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем необходимые системные библиотеки (если требуется)
RUN apt-get update && apt-get install -y \
    python3-dev \
    libx11-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем pynput отдельно
RUN pip install --no-cache-dir pynput

# Копируем все остальные файлы в контейнер
COPY . .

# Указываем команду для запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
