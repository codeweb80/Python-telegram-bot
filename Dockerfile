FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

# Environment variables should be provided externally
# TELEGRAM_TOKEN: your bot token
# WHATSAPP_CHANNEL_LINK: your WhatsApp invite link
CMD ["python", "main.py"]
