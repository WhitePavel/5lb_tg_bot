import datetime
import sqlite3 as sq


import requests
import dict_achent as dba
from request_my_sklad import day_cassir_for_retail ,headers
from administration_DB import employ_db
from HTTP_FOR_TODAY_SHOP import current_data,id_store
def database():
    for i in range(1,8):
        current_data_genetrator = datetime.datetime.now().strftime(f'%Y-%m-0{i}')
        All = f"https://api.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={current_data_genetrator} 00:00:00&momentTo={current_data_genetrator} 23:59:59"
        with sq.connect("/Users/pavelprosvetov/Desktop/Python_work/5lb_aiogram_bot/db/employ.db") as con:  # обновлнение смен за день
            cur = con.cursor()
            for emplou in employ_db(All):
                cur.execute(
                    f"""UPDATE employ SET count_work_shift_month = count_work_shift_month + 1 WHERE name ='{emplou}' """)
                if current_data_genetrator == current_data:
                    cur.execute(f"""UPDATE employ SET count_work_shift_day = count_work_shift_day + 1 WHERE name ='{emplou}' """)

def obnulenie():
    with sq.connect("/Users/pavelprosvetov/Desktop/Python_work/5lb_aiogram_bot/db/employ.db") as con:
        cur = con.cursor()
        cur.execute("""UPDATE employ SET count_work_shift_day = 0""")
        cur.execute("""UPDATE employ SET count_work_shift_month = 0""")

def achent_apotheka():
    for store in id_store:
        for i in range(1, 8):
            current_data_genetrator = datetime.datetime.now().strftime(f'%Y-%m-0{i}')
            url = ("https://api.moysklad.ru/api/remap/1.2/report/profit/byproduct" 
               f"?momentFrom={current_data_genetrator} 00:00:00&momentTo={current_data_genetrator} 23:59:59"
               f"&filter=store=https://api.moysklad.ru/api/remap/1.2/entity/store/{store}")

            response = requests.request("GET", url, headers=headers).json()
            for i in response["rows"]:
                if i["assortment"]["meta"]["href"][53:] in dba.src:

                    return i["assortment"]["meta"]["href"][53:],day_cassir_for_retail(f"https://api.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={current_data} 00:00:00"
                                                "&filter=store=https://api.moysklad.ru/api/remap/1.2/entity/store/"
                                                f"{store}"), int(i["sellQuantity"])
                else:
                    return "Сегодня пусто"

def main():
    obnulenie()
    database()
    achent_apotheka()

if __name__ =="__main__":
    main()