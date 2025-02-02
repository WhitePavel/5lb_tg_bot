from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from administration_DB import requsets_DB_retail
import request_my_sklad as req
import HTTP_FOR_TODAY_SHOP as HTTP
import keyboard as kb                         # импорт клавиатуры

router = Router()

@router.message(F.from_user.id != 1007925403)
async def handle_unwanted_users(message: Message):
    await message.answer(text="не туда ты попал,дружок!")
    await message.answer_photo("https://cs.pikabu.ru/post_img/2013/12/22/6/1387695893_547621352.jpg",caption="дай угадаю,кто-то украл твой сладкий рулет?")

@router.message(Command('start'))                                           # в обработчик можно поместить любую команду
async def get_help(message: Message):                                       # например "help" , "start", "reg" и т.д.
    await message.answer("Привет,выбери что тебя интересует",reply_markup=kb.main)           # здесь ставим на первую комнду основную клаву

@router.message(F.text == "Магазины🛍")                                      # В F.text храниться сообщение которое пришло от пользователя
async def how_are_you(message: Message):
    await message.answer("Выбери за какой период",reply_markup=kb.shop)

@router.message(F.text == "Сотрудники👥")
async def period_employ(message: Message):
    await message.answer("Выбери интересующий период",reply_markup=kb.employ)

@router.message(F.text == "Акценты💰")
async def acchent(message: Message):
    await message.answer(f"""Действующие акценты:
<b>Первый живой коллаген (300р)</b>
<b>Апотека картон (400р)</b>
<b>Апотека стекло (300р)</b>
<b>Лабелло (500р)</b>
<b>Marine Collagen 1+1 (200)</b>
""",parse_mode="HTML",reply_markup= await kb.employy_achent_mounth())



@router.callback_query(F.data == 'today_shop')         # обрабатываем магазины на сегодня
async def catalog(callback:CallbackQuery):
    await callback.answer('')
    await callback.message.answer(text="Магазины:",reply_markup= await kb.store_today())
    await callback.message.delete()
    await callback.message.answer(f"""
    {req.requests_all(HTTP.ALL_TODAY)}
    """)

@router.callback_query(F.data == 'month_shop')         #
async def catalog(callback:CallbackQuery):
    await callback.answer('')
    await callback.message.answer(text="Магазины:",reply_markup= await kb.store_mount())
    await callback.message.delete()
    await callback.message.answer(f"""
    {req.requests_all(HTTP.ALL_MOUNTH)}
    """)

@router.callback_query(F.data == 'today_employ')
async def catalog(callback:CallbackQuery):
    await callback.answer('')
    await callback.message.answer(text="Продавцы:",reply_markup= await kb.employy_today())
    await callback.message.delete()

@router.callback_query(F.data == 'mouth_employ')
async def catalog(callback:CallbackQuery):
    await callback.answer('')
    await callback.message.answer(text="Продавцы:",reply_markup= await kb.employy_mounth())
    await callback.message.delete()

@router.callback_query(F.data.regexp(r"achent_,*"))
async def data_in_achent(callback:CallbackQuery):
    await callback.answer("")
    await callback.message.answer(f"""10% от выручки{req.achent_and_employ_pay(callback.data)}
Оклад за смены{requsets_DB_retail(callback.data[7:])} 
Акцентные позиции""")
