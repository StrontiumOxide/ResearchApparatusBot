from aiogram import Router, types as tp
from aiogram.filters import Command
from utils.config import process_user

router = Router()

@router.message(Command(commands=['archive_cleaning']))
async def cleaning_archive(message: tp.Message) -> None:

    '''
    Корутина по обработке команды /archive_cleaning
    '''
    
    user_id = message.from_user.id
    if user_id in process_user:
        del process_user[user_id]
        await message.answer(text='Ваш архив очищен 🚮')
    else:
        await message.answer(text='Ваш архив и так пуст 👍')
