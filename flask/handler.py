import datetime
import json
import time

import requests
from pprint import pprint

def handl():
    url = "https://api.getscreen.ru/v1/agents/list"
    params = {
        "apikey" : "ZiBE26rKEfUW5JhEZUqTPgMZxhZMrztZ0ia7lhQGUqLADo40vyRS6R2byGq2QQii"
    }
    r = requests.get(url=url, params=params)
    data = json.loads(r.text)
    mas_id = []
    for i in range(len(data)):
        mas_id.append(data[i]["id"])

    print(mas_id)


    clients = []


    for i in range(len(mas_id)):
        url2 = "https://api.getscreen.ru/v1/agents/info"
        params2 = {
            "apikey": "ZiBE26rKEfUW5JhEZUqTPgMZxhZMrztZ0ia7lhQGUqLADo40vyRS6R2byGq2QQii",
            "agent_id": mas_id[i]
        }
        r2 = requests.get(url=url2, params=params2)
        text = json.loads(r2.text)



        data = text["data"]
        geo = text["data"]["geo"]
        hardware = text["data"]["hardware"]
        LogicalDisks = text["data"]["hardware"]["LogicalDisks"]
        HDD = text["data"]["hardware"]["HDD"]
        # try:
        #     sessions = text["data"]["sessions"]["last"]
        # except:
        #     print("Ошибка сессии: " + str(i))
        #
        # sessions_total = text["data"]["sessions"]["total"]

        disks = ""
        for j in LogicalDisks:
            disks += f"{list(j.values())[0]}\n"

        hdd_names = ''
        for j in HDD:
            hdd_names += f"{list(j.values())[0]}\n"

        size_disks = ''
        for j in LogicalDisks:
            size_disks += f"{list(j.values())[4]}\n"

        freespace_disks = ''
        for j in LogicalDisks:
            freespace_disks += f"{list(j.values())[2]}\n"

        client_dict = {
            list(data.keys())[0]: list(data.values())[0],  # id
            list(data.keys())[1]: list(data.values())[1],  # name
            list(data.keys())[6]: datetime.datetime.fromtimestamp(list(data.values())[6]).strftime('%Y-%m-%d %H:%M:%S'),
            # lasttime
            list(geo.keys())[0]: list(geo.values())[0],  # ip
            list(geo.keys())[3]: list(geo.values())[3],  # country
            list(geo.keys())[4]: list(geo.values())[4],  # region
            list(geo.keys())[5]: list(geo.values())[5],  # city
            list(data.keys())[12]: list(data.values())[12],  # version
            list(data.keys())[13]: list(data.values())[13],  # online
            list(hardware.keys())[0]: list(hardware.values())[0],  # BIOS
            list(hardware.keys())[2]: list(hardware.values())[2],  # BIOSVersion
            list(hardware.keys())[3]: list(hardware.values())[3],  # CPU
            list(hardware.keys())[4]: list(hardware.values())[4],  # CPUCores
            list(hardware.keys())[7]: list(hardware.values())[7],  # CPUSpeed
            list(hardware.keys())[9]: "\n".join(list(hardware.values())[9]),  # IP_MAC
            list(hardware.keys())[10]: list(hardware.values())[10],  # model
            list(hardware.keys())[11]: list(hardware.values())[11],  # coputer_name
            "DISKS": disks,  # disks
            "HDD names": hdd_names,  # disks_name
            "Size": size_disks,  # size_disks
            "FreeSpace": freespace_disks,  # free_spase
            list(hardware.keys())[25]: list(hardware.values())[25],  # os_version
            list(hardware.keys())[34]: list(hardware.values())[34],  # videoname
            list(hardware.keys())[35]: list(hardware.values())[35],  # videoram
            #list(sessions.keys())[0]: list(sessions.values())[0],  # sessions_last_id
            #list(sessions.keys())[1]: list(sessions.values())[1],  # sessions_last_start
            #list(sessions.keys())[1]: list(sessions.values())[1],  # sessions_last_stop
            #"Last Total": sessions_total  # sessions_last_total
        }
        clients.append(client_dict)



    file = open("data.json", "w")
    json.dump(clients,  file, indent=4)
    file.close()

while True:
    time.sleep(43200)
    handl()
    print(f"Success: {datetime.datetime.now()}")

