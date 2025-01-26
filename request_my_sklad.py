import os
import datetime
import requests
from dotenv import load_dotenv
import json
import HTTP_FOR_TODAY_SHOP as HTTP

load_dotenv()
current_data = datetime.datetime.now().strftime('%Y-%m-%d')
headers = {'Authorization': os.getenv("MY_SKLAD_TOKEN")}
current_data_mounth = datetime.datetime.now().strftime('%Y-%m-01')

def requests_all_stores() -> list:
    list_store = []
    url = "https://api.moysklad.ru/api/remap/1.2/entity/store"

    response = requests.request("GET", url, headers=headers)
    stores = json.loads(response.text)["rows"]

    for store in stores:
        list_store.append(store["name"])
    return list_store

def requests_all(url) -> str:
    sell_Cost_Sum,profit,sales_count,sell_sum = 0,0,0,0
    url = url

    response = requests.request("GET", url, headers=headers)

    list_seller = json.loads(response.text)
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
        salesCount = data_json["rows"][0]["salesCount"]
        salesAvgCheck = data_json["rows"][0]["salesAvgCheck"]/100
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
    emloy_list = []
    url=url
    response = requests.request("GET", url, headers=headers).text
    data_json = json.loads(response)

    for name in data_json["rows"]:
        emloy_list.append(name["employee"]["name"])

    return emloy_list

def byemployee_array():
    emloy_list = []
    url = f"https://api.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={current_data_mounth} 00:00:00"
    response = requests.request("GET", url, headers=headers).text
    data_json = json.loads(response)

    for name in data_json["rows"]:
        name_today = "m"+name["employee"]["name"]
        name_mounth = "t"+name["employee"]["name"]
        emloy_list.append(name_today)
        emloy_list.append(name_mounth)

    return tuple(emloy_list)

def byemployee_callback_today(callback_name):
    url = f"https://api.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={current_data} 00:00:00"
    response = requests.request("GET", url, headers=headers).text
    data_json = json.loads(response)
    for name in data_json["rows"]:
        if name["employee"]["name"] == callback_name[1:] and len(data_json["rows"]) != 0:
            # return name["salesCount"]
            salesCount = name["salesCount"]
            salesAvgCheck = name["salesAvgCheck"] / 100
            sellSum = name["sellSum"] / 100
            sellCostSum = name["sellCostSum"] / 100
            profit = name["profit"] / 100
            margin_products = round(name["margin"] * 100, 1)
            salesMargin = round(name["salesMargin"] * 100, 1)

            return f"""Количество чеков за сегодня: {salesCount}

Средний чек: {salesAvgCheck}

Общая сумма продаж: {sellSum}

Сумма себестоимости: {sellCostSum}

Выручка: {profit}

Рентабельность товара: {margin_products}%

Рентабельность продаж: {salesMargin}%"""

def byemployee_callback_mounth(callback_name):
    url = f"https://api.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={current_data_mounth} 00:00:00"
    response = requests.request("GET", url, headers=headers).text
    data_json = json.loads(response)
    for name in data_json["rows"]:
        if name["employee"]["name"] == callback_name[1:] and len(data_json["rows"]) != 0:
            # return name["salesCount"]
            salesCount = name["salesCount"]
            salesAvgCheck = name["salesAvgCheck"] / 100
            sellSum = name["sellSum"] / 100
            sellCostSum = name["sellCostSum"] / 100
            profit = name["profit"] / 100
            margin_products = round(name["margin"] * 100, 1)
            salesMargin = round(name["salesMargin"] * 100, 1)

            return f"""Количество чеков за месяц: {salesCount}

Средний чек: {salesAvgCheck}

Общая сумма продаж: {sellSum}

Сумма себестоимости: {sellCostSum}

Выручка: {profit}

Рентабельность товара: {margin_products}%

Рентабельность продаж: {salesMargin}%"""
