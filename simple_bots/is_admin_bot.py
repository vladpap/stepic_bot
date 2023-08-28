from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.types import Message
from environs import Env


env = Env()              # Создаем экземпляр класса Env
env.read_env()           # Методом read_env() читаем файл .env

bot_token = env('BOT_TOKEN')
# Выключаем у бота бэкэнд. Отправляем в браузере запрос:
# https://api.telegram.org/bot<token>/getUpdates

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher()

# Список с ID администраторов бота. !!!Замените на ваш!!!
admin_ids: list[int] = [173901673]


# Собственный фильтр, проверяющий юзера на админа
class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        # В качестве параметра фильтр принимает список с целыми числами
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids


# Этот хэндлер будет срабатывать, если апдейт от админа
@dp.message(IsAdmin(admin_ids))
async def answer_if_admins_update(message: Message):
    await message.answer(text='Вы админ')


# Этот хэндлер будет срабатывать, если апдейт не от админа
@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='Вы не админ')


if __name__ == '__main__':
    dp.run_polling(bot)
