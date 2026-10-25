import os
import requests

# --- КОНФИГУРАЦИЯ И СЛОВАРИ ---

# Словарь тегов по темам
TAGS_BY_TOPIC = {
    "политика": ["#политика", "#экономика", "#госрешения"],
    "технологии": ["#технологии", "#инновации", "#IT"],
    "культура": ["#культура", "#искусство", "#афиша"],
    "спорт": ["#спорт", "#футбол", "#хоккей"]
}

# --- ФУНКЦИИ ФОРМАТИРОВАНИЯ ---

def format_news_text(topic, title, summary, source, extra_info=""):
    """
    Формирует текст поста для Telegram в зависимости от темы.
    """
    tags = TAGS_BY_TOPIC.get(topic, ["#новости"])
    hashtags = " ".join(tags)

    # Базовые строки для разных тем
    if topic == "политика":
        header = f"🏛 В России: {title}"
        context_line = f"\n📉 Что это значит: {extra_info}" if extra_info else ""
        reaction_line = "\n💬 Реакция: Эксперты оценивают последствия для рынка."
    elif topic == "технологии":
        header = f"🚀 Технологии: {title}"
        context_line = f"\n⚡ Главное: {extra_info}" if extra_info else ""
        reaction_line = "\n💡 Зачем это важно: Решение применимо в промышленности и на удалённых объектах."
    elif topic == "культура":
        header = f"🎭 Культура: {title}"
        context_line = f"\n🌟 Почему это важно: {extra_info}" if extra_info else ""
        reaction_line = "\n🎫 Билеты: Уточняйте на сайте организатора."
    elif topic == "спорт":
        header = f"⚽ Спорт: {title}"
        context_line = f"\n🔥 Главное: {extra_info}" if extra_info else ""
        reaction_line = "\n🗓 Дальше: Следите за расписанием матчей."
    else:
        # Если тема неизвестна, используем универсальный формат
        header = title
        context_line = ""
        reaction_line = ""

    return (
        f"{header}\n\n"
        f"{summary}\n"
        f"{context_line}\n"
        f"{reaction_line}\n\n"
        f"📎 Источник: {source}\n\n"
        f"{hashtags}"
    )

# --- ФУНКЦИИ ОТПРАВКИ В TELEGRAM ---

def send_telegram_text_post(token, chat_id, text):
    """Отправляет текстовый пост."""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"  # Или "HTML", если используешь HTML-теги
    }
    try:
        resp = requests.post(url, json=payload)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка отправки текста: {e}")
        return None

def send_telegram_photo_post(token, chat_id, caption, photo_path):
    """Отправляет пост с фото."""
    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    
    if not os.path.exists(photo_path):
        print(f"Файл не найден: {photo_path}")
        return None

    with open(photo_path, "rb") as photo:
        data = {"chat_id": chat_id, "caption": caption}
        files = {"photo": photo}
        try:
            resp = requests.post(url, data=data, files=files)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка отправки фото: {e}")
            return None

# --- ОСНОВНОЙ ЦИКЛ (ПРИМЕР) ---

def main():
    # Получаем токен и ID чата из переменных окружения
    # Обязательно добавь их в .env или в настройки GitHub Actions
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("Ошибка: Не заданы TELEGRAM_BOT_TOKEN или TELEGRAM_CHAT_ID в переменных окружения!")
        return

    # --- ИМИТАЦИЯ ПОЛУЧЕНИЯ НОВОСТЕЙ (ЗАМЕНИ ЭТОТ БЛОК НА СВОЙ get_news()) ---
    # Здесь мы создаем список новостей для теста. В реальном коде ты будешь брать это из API или БД.
    news_items = [
        {
            "topic": "политика",
            "title":
