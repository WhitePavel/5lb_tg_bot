import os
import requests
import json
from dotenv import load_dotenv
import db.dict_achent as dba
from HTTP_FOR_TODAY_SHOP import current_data,current_data_mounth,id_store

load_dotenv()
headers = {'Authorization': os.getenv("MY_SKLAD_TOKEN")}
def requests_all_stores() -> list:                # запрос на получаение складов
    list_store = []
    url = "https://api.moysklad.ru/api/remap/1.2/entity/store"   # используется для клавиатуры создания складов
    response = requests.request("GET", url, headers=headers)

    stores = json.loads(response.text)["rows"]
    for store in stores:
        list_store.append(store["name"])
    return list_store



def requests_all(url) -> str:
    sell_Cost_Sum,profit,sales_count,sell_sum = 0,0,0,0
    url = url
    response = requests.request("GET", url, headers=headers)

    list_seller = json.loads(response.text)               # используется для получения отчётов за сегодня и за месяц
    for i in list_seller["rows"]:
        sales_count += i["salesCount"]
        sell_Cost_Sum += i["sellCostSum"]/100
        profit += i["profit"]/100
        sell_sum +=i["sellSum"]/100

    return (f"""Количество чеков: {sales_count}
    
Общая сумма продаж: {round(sell_sum,1)}р

Общая выручка: {round(profit,1)}р

Сумма себестоимости: {round(sell_Cost_Sum,1)}р""")


def shop(url) -> str:
    url = url

    response = requests.request("GET", url, headers=headers).text

    data_json = json.loads(response)
    if len(data_json["rows"]) != 0:
        salesCount = data_json["rows"][0]["salesCount"]              # используется для формирования отчёта по магазинам
        salesAvgCheck = data_json["rows"][0]["salesAvgCheck"]/100    # за день или за месяц
        sellSum = data_json["rows"][0]["sellSum"]/100
        sellCostSum = data_json["rows"][0]["sellCostSum"]/100
        profit = data_json["rows"][0]["profit"]/100
        margin_products = round(data_json["rows"][0]["margin"]*100,1)
        salesMargin = round(data_json["rows"][0]["salesMargin"]*100,1)


        return f"""Количество чеков: {salesCount}
    
    Средний чек: {salesAvgCheck}
    
    Общая сумма продаж: {sellSum}
    
    Сумма себестоимости: {sellCostSum}
    
    Выручка: {profit}
    
    Рентабельность товара: {margin_products}%
    
    Рентабельность продаж: {salesMargin}%"""
    else:
        return "Видимо сегодня продаж не было("


def byemployee(url):
    emloy_list = []       # получаем список сотрудников за нужные промежутки времени формирует клаву
    url=url
    response = requests.request("GET", url, headers=headers).text
    data_json = json.loads(response)

    for name in data_json["rows"]:
        emloy_list.append(name["employee"]["name"])

    return emloy_list

def byemployee_array():
    emloy_list = []
    url = (f"https://api.moysklad.ru/api/remap/1.2/report/profit/byemployee"
           f"?momentFrom={current_data_mounth} 00:00:00")
    response = requests.request("GET", url, headers=headers).text
    data_json = json.loads(response)

    for name in data_json["rows"]:                            # получаем наполняем обработчик callback
        name_today = "m"+name["employee"]["name"]
        name_mounth = "t"+name["employee"]["name"]
        emloy_list.append(name_today)
        emloy_list.append(name_mounth)


    return tuple(emloy_list)

def byemployee_callback_today(callback_name):
    if callback_name[0] == "t":
        url = (f"https://api.moysklad.ru/api/remap/1.2/report/profit/byemployee"
               f"?momentFrom={current_data} 00:00:00")
        time_moment ="сегодня"
    else:
        url = f"https://api.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={current_data_mounth} 00:00:00"
        time_moment = "месяц"

    response = requests.request("GET", url, headers=headers).text
    data_json = json.loads(response)
    for name in data_json["rows"]:
        if name["employee"]["name"] == callback_name[1:] and len(data_json["rows"]) != 0:
            # return name["salesCount"]
            salesCount = name["salesCount"]
            salesAvgCheck = name["salesAvgCheck"] / 100   # считаем выручку сотрудников за день
            sellSum = name["sellSum"] / 100
            sellCostSum = name["sellCostSum"] / 100
            profit = name["profit"] / 100
            margin_products = round(name["margin"] * 100, 1)
            salesMargin = round(name["salesMargin"] * 100, 1)

            return f"""Количество чеков за {time_moment}: {salesCount}

Средний чек: {salesAvgCheck}

Общая сумма продаж: {sellSum}

Сумма себестоимости: {sellCostSum}

Выручка: {profit}

Рентабельность товара: {margin_products}%

Рентабельность продаж: {salesMargin}%"""



def achent_and_employ_pay(callback_name):
    url = f"https://api.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={current_data_mounth} 00:00:00"
    response = requests.request("GET", url, headers=headers).text
    data_json = json.loads(response)
    for dict_employ in data_json["rows"]:
        if dict_employ["employee"]["name"] == callback_name[7:]:            # подсчёт по 10% от выручки магазина
            return dict_employ["profit"]//1000


def day_cassir_for_retail(url_store):
    response = requests.request("GET", url_store, headers=headers).text  # вывод кассира магазина сегодня
    data_json = json.loads(response)
    for dict_employ in data_json["rows"]:
       return dict_employ["employee"]["name"]

def achent_podschet_apotheca():
    for store in id_store:
        url = ("https://api.moysklad.ru/api/remap/1.2/report/profit/byproduct" 
               f"?momentFrom={current_data} 00:00:00"
               f"&filter=store=https://api.moysklad.ru/api/remap/1.2/entity/store/{store}")

        response = requests.request("GET", url, headers=headers).json()
        for i in response["rows"]:
           if i["assortment"]["meta"]["href"][53:] in dba.glass:
               id_apotheka_glass = i["assortment"]["meta"]["href"][53:]
               return print(id_apotheka_glass)
           elif i["assortment"]["meta"]["href"][53:] in dba.carton:
               id_apotheka_carton = i["assortment"]["meta"]["href"][53:]
               return print("картон",id_apotheka_carton)





def main():
    achent_podschet_apotheca()


if __name__ =="__main__":
    main()

