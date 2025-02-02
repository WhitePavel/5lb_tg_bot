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



dict_url_for_achent = {"url_ryzanka":(f"https://api.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={current_data} 00:00:00"
                                      "&filter=store=https://api.moysklad.ru/api/remap/1.2/entity/store/ce3b6c3b-ece0-11ee-0a80-16c4000b5fca"),

                       "url_AVENU":(f"https://api.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={current_data} 00:00:00"
                           "&filter=store=https://api.moysklad.ru/api/remap/1.2/entity/store/0542237a-ece1-11ee-0a80-109c000b87f5"),

                       "url_metropolis":(f"https://api.moysklad.ru/api/remap/1.2/report/profit/byemployee?momentFrom={current_data} 00:00:00"
                                         "&filter=store=https://api.moysklad.ru/api/remap/1.2/entity/store/84d3b1bb-db2d-11ee-0a80-17180002b320")}

apotheka_glass=("55c69c68-e775-11ee-0a80-144e0005ff7e","faaf6e9d-edad-11ee-0a80-06480000d3c3",   # 5хтп ,антиоксидант(грибы)
                "db3a5808-ee78-11ee-0a80-15f200217ab2","db3e053f-ee78-11ee-0a80-15f200217ab6",   # блум ночь и день
                "55e56bf8-e775-11ee-0a80-144e0005ff96","db526c1f-ee78-11ee-0a80-15f200217aba",   # браин комплекс, калм ейс(грибы)
                "55cd47e6-e775-11ee-0a80-144e0005ff82","db9b4a17-ee78-11ee-0a80-15f200217abe",   # q10 ,Cognitive Enhancer
                "18e91d6f-009e-11ef-0a80-10b7003d7b7e","dbb6ffdd-ee78-11ee-0a80-15f200217ad2",   # коллаген, comfort design(грибы)
                "55ead06b-e775-11ee-0a80-144e0005ff9a","dc6442a7-ee78-11ee-0a80-15f200217b36",   # фолиевая кислота, immunoglukan
                "dd1f4b7d-ee78-11ee-0a80-15f200217b67","dd250a1f-ee78-11ee-0a80-15f200217b6c",   # mushroom blend, nerwe system
                "55d2526d-e775-11ee-0a80-144e0005ff86","55c190ae-e775-11ee-0a80-144e0005ff7a",   # omega3 omega3-6-9
                "55d715f1-e775-11ee-0a80-144e0005ff8a","55efa98b-e775-11ee-0a80-144e0005ff9e",   # selenium, vitamin A
                "55db590f-e775-11ee-0a80-144e0005ff8e","55e0329a-e775-11ee-0a80-144e0005ff92",   # Vitamin C lemon, Vitamin C 2
                "069fda3c-226d-11ef-0a80-0f280011e054","55f477ef-e775-11ee-0a80-144e0005ffa2"    # vitamin D, Vitamin E
                "dea08a39-ee78-11ee-0a80-15f200217c0c","" # workout Boost
                )

apotheca_carton=("5615c912-e775-11ee-0a80-144e0005ffbe","5638180c-e775-11ee-0a80-144e0005ffda",  # актив мультивит, анти-инфломатори
                 "56327dd4-e775-11ee-0a80-144e0005ffd6","562cc773-e775-11ee-0a80-144e0005ffd2",  # холестерол, daily energy
                 "dbf264e3-ee78-11ee-0a80-15f200217ad6","fa82b632-edad-11ee-0a80-06480000d3bb",  # detox ,healthy design
                 "562287c8-e775-11ee-0a80-144e0005ffca","561e4f61-e775-11ee-0a80-144e0005ffc6",  # imunse support join complex
                 "560d6e67-e775-11ee-0a80-144e0005ffb6","5619b7a5-e775-11ee-0a80-144e0005ffc2",  # libido potency, memory complex
                 "5641ae72-e775-11ee-0a80-144e0005ffe2","167df49a-3ee0-11ef-0a80-0b16001933cc",  # osteprotector, pergance+
                 "55f9e2e7-e775-11ee-0a80-144e0005ffa6","5611c903-e775-11ee-0a80-144e0005ffba",  # preovention of osteoporosis,skin nails hair
                 "55ff84a6-e775-11ee-0a80-144e0005ffaa","563d4e23-e775-11ee-0a80-144e0005ffde",  # slim complex,sress managment
                 "56088bcb-e775-11ee-0a80-144e0005ffb2","5604691e-e775-11ee-0a80-144e0005ffae",  # VITAMEN, Vitawomen
                 "5627538c-e775-11ee-0a80-144e0005ffce","" # with antibiotic therapy
                 )
labello = ()