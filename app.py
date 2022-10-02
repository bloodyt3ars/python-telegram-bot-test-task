from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN, ADMIN_ID

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


async def on_startup(dp):
    await bot.send_message(chat_id=ADMIN_ID, text="Бот начал свою работу")

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dispatcher=dp, on_startup=on_startup)
