from aiogram.types import Message
import mysql.connector

from config import CONFIG
from app import bot, dp


@dp.message_handler(commands=['start'])
async def process_start_command(message: Message):
    await message.answer(f"Привет {message.from_user.full_name}. Это тестовое задание :)")


@dp.message_handler()
async def get_message(message: Message):
    my_data_base = mysql.connector.connect(**CONFIG)
    my_cursor = my_data_base.cursor()
    chat_id = message.chat.id
    text = message.text
    insert_main_query = f"INSERT INTO main (chat_id, text_message) VALUES ('{chat_id}', '{text}')"
    my_cursor.execute(insert_main_query)
    my_data_base.commit()
    select_main_query = f"SELECT text_message from main where chat_id = {chat_id}"
    my_cursor.execute(select_main_query)
    for row in my_cursor.fetchall():
        await bot.send_message(chat_id=chat_id, text=row[0])
        print(row[0])
    my_cursor.close()
    my_data_base.close()




