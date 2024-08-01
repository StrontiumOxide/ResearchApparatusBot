from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Сканер 📡', callback_data='scaner'),
            InlineKeyboardButton(text='Архив 🗂', callback_data='archive')
        ]
    ]
)
