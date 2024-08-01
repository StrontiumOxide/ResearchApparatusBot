import asyncio
from aiogram import Router, types as tp, F
from aiogram.fsm.context import FSMContext
from random import randint
from utils.states import CodeData
from utils.config import process_user

router = Router()

@router.callback_query(F.data == 'scaner')
async def scaner(callback: tp.CallbackQuery, state: FSMContext) -> None:

    '''
    Корутина по обработке сканера.
    '''
        
    await state.clear() # Очищает предыдующие состояние.

    await callback.answer()

    await callback.message.answer(
        text='Введите код исследования 🔢'
    )

    await state.set_state(CodeData.code)


@router.message(CodeData.code)
async def get_code(message: tp.Message, state: FSMContext) -> None:

    '''
    Корутина по получении кода иследования.
    '''

    await state.clear()

    await message.answer(
        text='Подготовка к сканированию... ⚒'
    )
    await asyncio.sleep(2)

    if message.text not in ['091283', '123026']:
        await message.answer(
            text='Объект сканирования не найден: <b>"Error object"</b>🚫\nНастройте исследовательский аппарат ⚒'
        )
        return
    
    if message.text == '091283':
        process_sleep = 5 + 1 * randint(0, 10)
        text = '''
Обнаружен объект неизвестного происхождения ❔
<blockquote>Код исследования: [0001]

Код объекта: [X]

Локация: [Северный район]

Форма объекта: [Растительность]

Описание: Среда объекта не агресивна, обнаружены скрытые свойства - длительное нахождение в среде может быть опасно для объекта исследования. Возможны проявления доминирования над разумом.

Указания для дальнейших операций: "Исследование в безопасной среде"</blockquote>
'''

    elif message.text == '123026':
        process_sleep = 5 + 1 * randint(0, 5)
        text = '''
Обнаружен объект неизвестного происхождения ❔
<blockquote>Код исследования: [0010]

Код объекта: [T]

Локация: [Центральный район]

Форма объекта: [Биологическая, мутация]

Описание: Объект биологического происхождения, в геноме объекта замечен мутаген ранее изученого типа - «T-Virus».</blockquote>
'''

    edit_msg = await message.answer(
        text=f'Начало сканирования 📡\nВремя сканирования: {process_sleep} мин. ⏳'
    )

    while True:
        await asyncio.sleep(60)
        process_sleep -= 1

        await edit_msg.edit_text(
            text=f'Начало сканирования 📡\nВремя сканирования: {process_sleep} мин. ⏳'
        )

        if process_sleep == 0:
            break

    await message.answer(
        text=text
    )

    user_id = message.from_user.id

    if user_id in process_user:
        if message.text not in process_user[user_id]:
            process_user[user_id].append(message.text)
    else:
        process_user[user_id] = [message.text]
