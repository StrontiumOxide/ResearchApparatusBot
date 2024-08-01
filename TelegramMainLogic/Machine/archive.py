from aiogram import Router, types as tp, F
from utils.config import process_user
from data.loader_file import load_file
from TelegramMainLogic.Greetings import greetings_kb as gkb
from TelegramMainLogic.Machine import machine_kb as kb

router = Router()

@router.callback_query(F.data == 'archive')
async def archive(callback: tp.CallbackQuery) -> None:

    '''
    Корутина по обработке архива.
    '''
    
    user_id = callback.from_user.id
    if user_id not in process_user:
        await callback.answer(
            text='В архиве нет данных ❌',
            show_alert=True
        )
        return
    
    await callback.message.edit_media(
        media=tp.InputMediaPhoto(
            media=load_file(category='photo', file_name='archive.jpg'),
            caption='<b>Архив</b>'
        ),
        reply_markup=kb.builder.archive_record(user_id=user_id)
    )


@router.callback_query(F.data == 'back')
async def back_handler(callback: tp.CallbackQuery) -> None:

    '''
    Корутина по обработке возвращения в главное меню.
    '''

    await callback.message.edit_media(
        media=tp.InputMediaPhoto(
            media=load_file(category='photo', file_name='machine.jpg'),
            caption='<b>Вас приветствует AIUmCorp. Выберите действие</b>'
        ),
        reply_markup=gkb.inline.start_kb
    )


@router.callback_query(F.data == 'flower')
async def flower_handler(callback: tp.CallbackQuery) -> None:

    '''
    Корутина по обработке возвращения в главное меню.
    '''

    text = '''
<b>Аномалия "Тирано Цветок" 🌹</b>

<b>Описание:</b>
<i>Аномалия природного типа. Мутировавший цветок. Излучает радиацию и свечение красного цвета -  по неизвестным причинам.</i>

<b>История:</b>
<i>Достоверно неизвестно каким образом растение попало на территорию ЧЗО. Вероятно, растение было сгенерировано в лабораториях ЧАЭС и отправлено в природную среду. Впервые был замечен в секторе #26.</i>

<b>Свойства:</b>
<i>Излучает радиацию и пси-поле в ореоле произростания, синтезирует рядом с собой артефакт "Мицелий".</i>
'''
    group_media = [
        tp.InputMediaPhoto(
            media=load_file(category='photo', file_name='flower_1.jpg'),
            caption=text
        ),
        tp.InputMediaPhoto(media=load_file(category='photo', file_name='flower_2.jpg')),
        tp.InputMediaPhoto(media=load_file(category='photo', file_name='flower_3.jpg')),
    ]

    await callback.answer(
        text='Информация выгружена из архива ⚠️',
        show_alert=True
    )

    await callback.message.answer_media_group(
        media=group_media
    )


@router.callback_query(F.data == 'bush')
async def flower_handler(callback: tp.CallbackQuery) -> None:

    '''
    Корутина по обработке возвращения в главное меню.
    '''

    text = '''
<b>Артефакт "Мицелий" 🍄</b>

<b>Описание:</b>
<i>Артефакт природного типа. Об этом свидетельствует внешний вид: стеклянный или пластиковый шар обвернутый ветвями растения у которого просходит синтез артефакта.</i>

<b>История:</b>
<i>Ранее не изучен и в зоне появился позже других.  Но уже приобрёл уникальное название "Мицелий". Видимо из-за сходства спор грибов.</i>

<b>Свойства:</b>
<i>Не имеет целебных свойств 
Через длительное время ношения на поясе зомбирует своего хозяина
Отпугивает мутантов*
*Это происходит из-за сильного ультразвукого сигнала в непосредственной близости к мутанту*</i>
'''

    group_media = [
        tp.InputMediaPhoto(
            media=load_file(category='photo', file_name='bush_1.jpg'),
            caption=text
        ),
        tp.InputMediaPhoto(media=load_file(category='photo', file_name='bush_2.jpg')),
        tp.InputMediaPhoto(media=load_file(category='photo', file_name='bush_3.jpg')),
    ]

    await callback.answer(
        text='Информация выгружена из архива ⚠️',
        show_alert=True
    )
    
    await callback.message.answer_media_group(
        media=group_media
    )


@router.callback_query(F.data == 'dna')
async def flower_handler(callback: tp.CallbackQuery) -> None:

    '''
    Корутина по обработке возвращения в главное меню.
    '''

    text = '''
<b>Образец «Т» 🧬</b>

<b>Описание:</b>
<i>Образец вируса «T»  ранее группой учёных Umbrella corp.</i>

<b>История:</b>
<i>В начале 90-х годов XX века, ученые из корпорации Umbrella начали исследование генетических мутаций с целью создания идеального биологического оружия. Вдохновленные работами по ДНК-манипуляциям и генетической инженерии, они обнаружили, что активные белки, приведенные в взаимодействие с нервными клетками, могут вызвать необратимые изменения в организме.</i>

<b>Свойства:</b>
<i>1. Мутагенные свойства: «Т» вирус способен вызывать глубокие мутации в организме хозяина, что не только изменяет его физические характеристики, но и влияет на психическое состояние.
2. Регенерация: Вирус обладает способностью восстанавливать поврежденные ткани, что делает зараженных более выносливыми и труднопробиваемыми. Это качество значительно увеличивает срок жизни исходных клеток.
3. Психическая агрессия: Зараженные «Т» вирусом теряют контроль над своим поведением и становятся агрессивными, часто проявляя склонность к насилию и хищническим инстинктам.</i>
'''

    group_media = [
        tp.InputMediaPhoto(
            media=load_file(category='photo', file_name='DNA_1.jpg'),
            caption=text
        ),
        tp.InputMediaPhoto(media=load_file(category='photo', file_name='DNA_2.jpg')),
    ]

    await callback.answer(
        text='Информация выгружена из архива ⚠️',
        show_alert=True
    )
    
    await callback.message.answer_media_group(
        media=group_media
    )
