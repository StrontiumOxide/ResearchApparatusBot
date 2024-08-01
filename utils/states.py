from aiogram.fsm.state import State, StatesGroup

class CodeData(StatesGroup):

    '''
    Класс для хранения информации для создания контента.
    '''

    code = State()
