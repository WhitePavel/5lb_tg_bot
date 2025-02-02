import sqlite3 as sq
import requests
import json
from request_my_sklad import headers
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
    with sq.connect("employ.db") as con:  # обновлнение смен за день
        cur = con.cursor()
        for emplou in employ_db(ALL_TODAY):
            if current_data == current_data_mounth:
                cur.execute(f"""UPDATE employ SET count_work_shift_day = 0 """)   # обнуляю смены так ка новый месяц
                cur.execute(
                    f"""UPDATE employ SET count_work_shift_day = count_work_shift_day + 1 WHERE name ='{emplou}' """)
                        # добовляю смены тем кто сегдня работал
                cur.execute(f"""UPDATE employ SET count_work_shift_month = 0 """)
                cur.execute(
                    f"""UPDATE employ SET count_work_shift_month = count_work_shift_month + 1 WHERE name ='{emplou}' """)

            else:
                cur.execute(
                    f"""UPDATE employ SET count_work_shift_day = count_work_shift_day + 1 WHERE name ='{emplou}' """)
                cur.execute(
                    f"""UPDATE employ SET count_work_shift_month = count_work_shift_month + 1 WHERE name ='{emplou}' """)


def requsets_DB_retail(callback):
    callback =re.sub(string=callback, pattern="[, .]",repl="")
    with sq.connect("employ.db") as con:  # обновлнение смен за день
        cur = con.cursor()
        cur.execute(f"""SELECT count_work_shift_month FROM employ WHERE name LIKE '{callback}' """)
        return cur.fetchall()[0][0] * 2000



def main():
    # filling_DB()
    pass
if __name__ == "__main__":
    main()
