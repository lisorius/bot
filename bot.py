import asyncio
import logging
from io import BytesIO

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import ContentTypeFilter
from aiogram.types import InputFile
from PIL import Image

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Токен вашего бота
TOKEN = '6891156935:AAGebRyO0ayEpyBgMOIJ4svxzM-ZDg2UgFs'

# Создание объектов Bot и Dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Обработчик сообщений с фото
@dp.message_handler(content_types=ContentTypeFilter(content_types=['photo']))
async def handle_docs_photo(message: types.Message):
    time.sleep(1)
    # Скачивание фото
    photo = message.photo[-1]
    await photo.download('r1.png')
    # Открытие изображения с помощью библиотеки Pillow
    img = Image.open('r1.png')
    # Уменьшение изображения в два раза
    resized_img = img.resize((img.width // 2, img.height // 2))
    # Сохранение уменьшенного изображения в буфер
    bio = BytesIO()
    resized_img.save(bio, format="PNG")
    bio.seek(0)
    # Отправка уменьшенного изображения пользователю
    await message.reply_photo(photo=bio)


async def main():
    # Запуск бота
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
