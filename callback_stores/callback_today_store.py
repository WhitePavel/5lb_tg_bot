
from aiogram import F, Router
from aiogram.types import CallbackQuery
import HTTP_FOR_TODAY_SHOP as HTTP
import request_my_sklad as req
import keyboard as kb                         # импорт клавиатуры

router_store_today = Router()
data_shop = {'tАшан Рязанка',"mАшан Рязанка",
             'tТЦ Авеню Юго-Западная',"mТЦ Авеню Юго-Западная",
             'tМетрополис',"mМетрополис",
             'tГлобус Медведково',"mГлобус Медведково",
             'tБеляево',"mБеляево"}

@router_store_today.callback_query(F.data == 'today_shop')         # обрабатываем магазины на сегодня
async def catalog(callback:CallbackQuery):
    await callback.answer('')
    await callback.message.answer(text="Магазины:",reply_markup= await kb.store_today())
    await callback.message.delete()
    await callback.message.answer(f"""
    {req.requests_all(HTTP.ALL_TODAY)}
    """)

@router_store_today.callback_query(F.data =='month_shop')        #
async def catalog(callback:CallbackQuery):
    await callback.answer('')
    await callback.message.answer(text="Магазины:",reply_markup= await kb.store_mount())
    await callback.message.delete()
    await callback.message.answer(f"""
    {req.requests_all(HTTP.ALL_MOUNTH)}
    """)


@router_store_today.callback_query(F.data.in_(data_shop))     # рязанка
async def catalog(callback:CallbackQuery):
        await callback.answer("")
        await callback.message.answer(text=f"""{callback.data[1:]}: 
    
{req.shop(callback.data)}""")



@router_store_today.callback_query(F.data.in_(req.byemployee_array()))         # каллбак показателей сотрудников
async def employ(callback:CallbackQuery):
    if callback.data[0] == "t":
        await callback.answer('')
        await callback.message.answer(f"""{callback.data[1:]}
        
{req.byemployee_callback_today(callback.data)}""")
    else:
        await callback.answer('')
        await callback.message.answer(f"""{callback.data[1:]}
        
{req.byemployee_callback_today(callback.data)}""")


    
      

