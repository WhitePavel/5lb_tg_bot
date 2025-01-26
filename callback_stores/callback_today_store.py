
from aiogram import F, Router
from aiogram.types import CallbackQuery
import HTTP_FOR_TODAY_SHOP as HTTP
import request_my_sklad as req

router_store_today = Router()

@router_store_today.callback_query(F.data.in_({'tАшан Рязанка',"mАшан Рязанка"}))
async def catalog(callback:CallbackQuery):
    if callback.data[0] == "t":
        await callback.message.answer(text=f"""Ашан Рязанка: 
    
{req.shop(HTTP.ASHAN_RYZANKA)}""")
    else:
        await callback.message.answer(text=f"""Ашан Рязанка: 
    
{req.shop(HTTP.ASHAN_RYZANKA_MOUNTH)}""")

@router_store_today.callback_query(F.data.in_({'tТЦ Авеню Юго-Западная',"mТЦ Авеню Юго-Западная"}))
async def catalog(callback:CallbackQuery):
    if callback.data[0] == "t":
        await callback.message.answer(text=f"""Авеню Юго-Западная: 
    
{req.shop(HTTP.AVENU)}""")
    else:
        await callback.message.answer(text=f"""Авеню Юго-Западная: 

{req.shop(HTTP.AVENU_MOUNTH)}""")

@router_store_today.callback_query(F.data.in_({'tМетрополис',"mМетрополис"}))
async def catalog(callback:CallbackQuery):
    if callback.data[0] == "t":
        await callback.message.answer(text=f"""Метрополис:
         
{req.shop(HTTP.METROPOLIS)}""")
    else:
        await callback.message.answer(text=f"""Метрополис: 

{req.shop(HTTP.METROPOLIS_MOUNTH)}""")

@router_store_today.callback_query(F.data.in_({'tГлобус Медведково',"mГлобус Медведково"}))
async def catalog(callback:CallbackQuery):
    if callback.data[0] == "t":
        await callback.message.answer(text=f"""Глобус Медведково: 
        
{req.shop(HTTP.GBLOBUS)}""")
    else:
        await callback.message.answer(text=f"""Глобус Медведково: 

{req.shop(HTTP.GBLOBUS_MOUNTH)}""")

@router_store_today.callback_query(F.data.in_({'tБеляево',"mБеляево"}))
async def catalog(callback:CallbackQuery):
    if callback.data[0] == "t":
        await callback.message.answer(text=f"""Беляево: 
    
{req.shop(HTTP.BELIAEVO)}""")
    else:
        await callback.message.answer(text=f"""Беляево: 

        {req.shop(HTTP.BELIAEVO_MOUNTH)}""")

@router_store_today.callback_query(F.data.in_(req.byemployee_array()))
async def employ(callback:CallbackQuery):
    if callback.data[0] == "t":
        await callback.message.answer(f"""{callback.data[1:]}
        
{req.byemployee_callback_today(callback.data)}""")
    else:
        await callback.message.answer(f"""{callback.data[1:]}
        
{req.byemployee_callback_mounth(callback.data)}""")


    
      

