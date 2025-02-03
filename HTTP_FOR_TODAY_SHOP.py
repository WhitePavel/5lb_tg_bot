import datetime

current_data = datetime.datetime.now().strftime('%Y-%m-%d')
current_data_mounth = datetime.datetime.now().strftime('%Y-%m-01')

ALL_TODAY = f"https://api.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={current_data} 00:00:00"
ALL_MOUNTH = f"https://api.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={current_data_mounth} 00:00:00"


ASHAN_RYZANKA = f"https://api.moysklad.ru/api/remap/1.2/report/profit/bycounterparty?filter=store=https://api.moysklad.ru/api/remap/1.2/entity/store/ce3b6c3b-ece0-11ee-0a80-16c4000b5fca&momentFrom={current_data} 00:00:00"
AVENU = f"https://api.moysklad.ru/api/remap/1.2/report/profit/bycounterparty?filter=store=https://api.moysklad.ru/api/remap/1.2/entity/store/0542237a-ece1-11ee-0a80-109c000b87f5&momentFrom={current_data} 00:00:00"
METROPOLIS = f"https://api.moysklad.ru/api/remap/1.2/report/profit/bycounterparty?filter=store=https://api.moysklad.ru/api/remap/1.2/entity/store/84d3b1bb-db2d-11ee-0a80-17180002b320&momentFrom={current_data} 00:00:00"
BELIAEVO = f"https://api.moysklad.ru/api/remap/1.2/report/profit/bycounterparty?filter=store=https://api.moysklad.ru/api/remap/1.2/entity/store/e202afd6-1e5f-11ef-0a80-0290000b158b&momentFrom={current_data} 00:00:00"
GBLOBUS = f"https://api.moysklad.ru/api/remap/1.2/report/profit/bycounterparty?filter=store=https://api.moysklad.ru/api/remap/1.2/entity/store/eba68415-e682-11ee-0a80-0e1200066c87&momentFrom={current_data} 00:00:00"

ASHAN_RYZANKA_MOUNTH = f"https://api.moysklad.ru/api/remap/1.2/report/profit/bycounterparty?filter=store=https://api.moysklad.ru/api/remap/1.2/entity/store/ce3b6c3b-ece0-11ee-0a80-16c4000b5fca&momentFrom={current_data_mounth} 00:00:00"
AVENU_MOUNTH = f"https://api.moysklad.ru/api/remap/1.2/report/profit/bycounterparty?filter=store=https://api.moysklad.ru/api/remap/1.2/entity/store/0542237a-ece1-11ee-0a80-109c000b87f5&momentFrom={current_data_mounth} 00:00:00"
METROPOLIS_MOUNTH = f"https://api.moysklad.ru/api/remap/1.2/report/profit/bycounterparty?filter=store=https://api.moysklad.ru/api/remap/1.2/entity/store/84d3b1bb-db2d-11ee-0a80-17180002b320&momentFrom={current_data_mounth} 00:00:00"
BELIAEVO_MOUNTH = f"https://api.moysklad.ru/api/remap/1.2/report/profit/bycounterparty?filter=store=https://api.moysklad.ru/api/remap/1.2/entity/store/e202afd6-1e5f-11ef-0a80-0290000b158b&momentFrom={current_data_mounth} 00:00:00"
GBLOBUS_MOUNTH = f"https://api.moysklad.ru/api/remap/1.2/report/profit/bycounterparty?filter=store=https://api.moysklad.ru/api/remap/1.2/entity/store/eba68415-e682-11ee-0a80-0e1200066c87&momentFrom={current_data_mounth} 00:00:00"

BYEMPLOE_MOUNTH = f"https://api.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={current_data_mounth} 00:00:00"
BYEMPLOE_TODAY = f"https://api.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={current_data} 00:00:00"


id_store = ("84d3b1bb-db2d-11ee-0a80-17180002b320","ce3b6c3b-ece0-11ee-0a80-16c4000b5fca")
