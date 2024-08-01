from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.config import process_user

def archive_record(user_id: int | str) -> InlineKeyboardMarkup:

    '''
    Данная функция строит и возвращает Inline-клавиатуру с записями из архива.
    '''

    keyboard = InlineKeyboardBuilder()

    for element in process_user[user_id]:

        if element == '091283':
            keyboard.row(
                InlineKeyboardButton(text='Аномалия "Тирано Цветок" 🌹', callback_data='flower'),
                InlineKeyboardButton(text='Мицелий 🍄', callback_data='bush'),
                width=1
            )

        elif element == '123026':
            keyboard.row(
                InlineKeyboardButton(text='Образец "Т" 🧬', callback_data='dna'),
                width=1
            )

    keyboard.row(InlineKeyboardButton(text='Назад ⤴️', callback_data='back'), width=1)

    return keyboard.as_markup()
