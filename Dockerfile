# Используем базовый образ
FROM python:3.9-slim

# Создаем пользователя с UID 10001
RUN useradd --uid 10001 --no-create-home --shell /bin/false webuser

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы
COPY web_server.py /app/
COPY obito.jpg /app/

# Меняем владельца файлов на пользователя webuser
RUN chown -R webuser:webuser /app

# Переключаемся на пользователя webuser
USER 10001

# Указываем порт, который будет слушать сервер
EXPOSE 8000

# Указываем команду для запуска сервера
CMD ["python3", "web_server.py"]
