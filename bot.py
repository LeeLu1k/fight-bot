from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command
from fastapi import FastAPI
import uvicorn
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")  # добавь токен бота в Railway Secrets

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

app = FastAPI()

# --- Telegram Commands ---
@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Играть 🕹", web_app=WebAppInfo(url="https://fight-bot-production.up.railway.app/web_app/index.html"))]
        ],
        resize_keyboard=True
    )
    await message.answer("Привет! Нажми на кнопку, чтобы играть с ботом.", reply_markup=keyboard)

# --- Game Webhook ---
@app.post("/webhook")
async def webhook(data: dict):
    # Тут можно обработать события из Web App
    print(data)
    return {"status": "ok"}

# --- Запуск FastAPI и Telegram Bot ---
if __name__ == "__main__":
    import asyncio
    from aiogram import executor

    async def main():
        from aiogram import Bot, Dispatcher
        import logging

        logging.basicConfig(level=logging.INFO)
        # Запуск бота
        await dp.start_polling(bot)

    asyncio.run(main())
