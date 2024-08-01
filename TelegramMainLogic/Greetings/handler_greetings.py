from aiogram import Router, types as tp
from aiogram.filters import CommandStart
from data.loader_file import load_file
from TelegramMainLogic.Greetings import greetings_kb as kb

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: tp.Message) -> None:

    '''
    Корутина по обработке команды /start.
    '''

    text_gretings = f'''
<b>Вас приветствует AIUmCorp. Выберите действие</b>
'''
    
    await message.answer_photo(
        photo=load_file(category='photo', file_name='machine.jpg'),
        caption=text_gretings,
        reply_markup=kb.inline.start_kb
    )
