from aiogram.types import ReplyKeyboardMarkup, KeyboardButton                         # для реплай
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton                  # для инлайн
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder        # для кнопок с запросом
import request_my_sklad as req
import HTTP_FOR_TODAY_SHOP as HTTP

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Магазины🛍')],
    [KeyboardButton(text='Сотрудники👥'),KeyboardButton(text='Акценты💰')],
    [KeyboardButton(text="Остатки на складах🗄")]],              # это передача в одну строку
    resize_keyboard=True,input_field_placeholder="выберите пункт меню")               # resize=для норм отображения
                                                                                      # placeholderдля надписи внутри окошка ввода

shop = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Сегодня",callback_data='today_shop'),
    InlineKeyboardButton(text='За месяц',callback_data='month_shop')]])       # нет запятых между списками(они будут в ряд),обработчик callback

employ = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Сегодня",callback_data='today_employ'),
    InlineKeyboardButton(text='За месяц',callback_data='mouth_employ')]])       #

async def store_today():
    keyboard = InlineKeyboardBuilder()
    for store in req.requests_all_stores():
        keyboard.button(text=store,callback_data=f"t{store.strip()}")
    return keyboard.adjust(2).as_markup()
async def store_mount():
    keyboard = InlineKeyboardBuilder()
    for store in req.requests_all_stores():
        keyboard.button(text=store,callback_data=f"m{store.strip()}")
    return keyboard.adjust(2).as_markup()

async def employy_today():
    keyboard = InlineKeyboardBuilder()
    for emplo in req.byemployee(HTTP.BYEMPLOE_TODAY):
        keyboard.button(text=emplo,callback_data=f"t{emplo.strip()}")
    return keyboard.adjust(2).as_markup()

async def employy_mounth():
    keyboard = InlineKeyboardBuilder()
    for emplo in req.byemployee(HTTP.BYEMPLOE_MOUNTH):
        keyboard.button(text=emplo,callback_data=f"m{emplo.strip()}")
    return keyboard.adjust(2).as_markup()

async def employy_achent_mounth():
    keyboard = InlineKeyboardBuilder()
    for emplo in req.byemployee(HTTP.BYEMPLOE_MOUNTH):
        keyboard.button(text=emplo,callback_data=f"achent_{emplo.strip()}")
    return keyboard.adjust(2).as_markup()