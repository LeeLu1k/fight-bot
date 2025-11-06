import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

# --- Переменные окружения ---
TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 8000))

# --- Инициализация бота ---
bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- FastAPI для Web App ---
app = FastAPI()
app.mount("/webapp", StaticFiles(directory="webapp"), name="webapp")

# --- Команда /start ---
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = ReplyKeyboardBuilder()
    kb.add(
        KeyboardButton(
            text="🎮 Играть",
            web_app=WebAppInfo(url=f"https://fight-bot-production.up.railway.app/webapp/index.html")
        )
    )
    await message.answer("Добро пожаловать в бой с ботом!", reply_markup=kb.as_markup(resize_keyboard=True))

# --- Обработка данных из Web App ---
@dp.message()
async def handle_webapp(message: types.Message):
    if message.web_app_data:
        await message.answer(f"Вы отправили данные из Web App: {message.web_app_data.data}")

# --- Запуск бота и FastAPI ---
async def start_bot():
    await dp.start_polling(bot)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())
    uvicorn.run(app, host="0.0.0.0", port=PORT)
