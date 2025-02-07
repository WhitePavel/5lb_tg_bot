import sqlite3 as sq
import requests
import json

from request_my_sklad import headers,achent_apotheka_today
import db.dict_achent as db

import re
from HTTP_FOR_TODAY_SHOP import ALL_TODAY,current_data,current_data_mounth

def employ_db(url):
    emloy_list = []
    url=url
    response = requests.request("GET", url, headers=headers).text
    data_json = json.loads(response)
    for name in data_json["rows"]:
        emloy_list.append(re.sub(string=name["employee"]["name"], pattern="[, .]",repl=""))

    return tuple(emloy_list)


def filling_DB():
    with sq.connect("/Users/pavelprosvetov/Desktop/Python_work/5lb_aiogram_bot/db/employ.db") as con:  # обновлнение смен за день
        cur = con.cursor()
        for emplou in employ_db(ALL_TODAY):
            if current_data == current_data_mounth:    # проверка на новый месяц
                cur.execute(f"""UPDATE employ SET count_work_shift_day = 0 """)   # обнуляю смены так ка новый месяц
                cur.execute(f"""UPDATE employ SET count_work_shift_day = count_work_shift_day + 1 WHERE name ='{emplou}' """)

                cur.execute(f"""UPDATE employ SET count_work_shift_month = 0 """)
                cur.execute(f"""UPDATE employ SET count_work_shift_month = count_work_shift_month + 1 WHERE name ='{emplou}' """)

            else:  # считает кто сегодня вышел на работу и заношу в базу данных
                cur.execute(f"""UPDATE employ SET count_work_shift_day = 0 """)
                cur.execute(f"""UPDATE employ SET count_work_shift_day = count_work_shift_day + 1 WHERE name ='{emplou}' """)
                cur.execute(f"""UPDATE employ SET count_work_shift_month = count_work_shift_month + 1 WHERE name ='{emplou}' """)


def requsets_DB_retail(callback):
    callback =re.sub(string=callback, pattern="[, .]",repl="")
    with sq.connect("/Users/pavelprosvetov/Desktop/Python_work/5lb_aiogram_bot/db/employ.db") as con:  # обновлнение смен за день
        cur = con.cursor()
        cur.execute(f"""SELECT count_work_shift_month FROM employ WHERE name LIKE '{callback}' """)
        return cur.fetchall()[0][0] * 2000

def request_db_pay_achent(callback):
    callback =re.sub(string=callback, pattern="[, .]",repl="")
    with sq.connect("/Users/pavelprosvetov/Desktop/Python_work/5lb_aiogram_bot/db/employ.db") as con:
        cur = con.cursor()
        cur.execute(f"SELECT apotheka_carton, apotheka_glass FROM employ WHERE name LIKE '{callback}'")
        return cur.fetchall()



def achent_position_add():

    with sq.connect("/Users/pavelprosvetov/Desktop/Python_work/5lb_aiogram_bot/db/employ.db") as con:
        cur = con.cursor()
        if achent_apotheka_today()[0] in db.carton.keys():
            cur.execute(f"UPDATE employ SET apotheka_carton = apotheka_carton + {achent_apotheka_today()[2]}"
                        f" WHERE name LIKE '{achent_apotheka_today()[1]}'")
        elif achent_apotheka_today()[0] in db.glass.keys():
            cur.execute(f"UPDATE employ SET apotheka_glass = apotheka_glass + {achent_apotheka_today()[2]}"
                        f" WHERE name LIKE '{achent_apotheka_today()[1]}'")
        else:
            return "Сегодня пусто"

def main():
    achent_position_add() # подсчёт за сегодня всех акцентов
    filling_DB()   # подсчет смен

if __name__ == "__main__":
    main()
