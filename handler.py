import datetime
import json
import requests

def last_id(text):
    try:
        sessions = text["data"]["sessions"]["last"]
        return list(sessions.values())[0]
    except:
        return ""


def last_start(text):
    try:
        sessions = text["data"]["sessions"]["last"]
        return datetime.datetime.fromtimestamp(list(sessions.values())[1]).strftime('%Y-%m-%d %H:%M:%S')
    except:
        return ""


def last_stop(text):
    try:
        sessions = text["data"]["sessions"]["last"]
        return datetime.datetime.fromtimestamp(list(sessions.values())[2]).strftime('%Y-%m-%d %H:%M:%S')
    except:
        return ""


def last_total(text):
    try:
        return text["data"]["sessions"]["total"]
    except:
        return ""


def handl():
    url = "https://api.getscreen.ru/v1/agents/list"
    params = {
        "apikey" : "Kqgd3KkXavcjCudX2Y9nY2ajBaFDXRnLHmO9EbeDytk6Di9pFCWNnbt6sjMq9CEZ"
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
            "apikey": "Kqgd3KkXavcjCudX2Y9nY2ajBaFDXRnLHmO9EbeDytk6Di9pFCWNnbt6sjMq9CEZ",
            "agent_id": mas_id[i]
        }
        r2 = requests.get(url=url2, params=params2)
        text = json.loads(r2.text)
        print(text)


        data = text["data"]
        geo = text["data"]["geo"]
        hardware = text["data"]["hardware"]
        LogicalDisks = text["data"]["hardware"]["LogicalDisks"]
        HDD = text["data"]["hardware"]["HDD"]


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
            "Имя клиента": list(data.values())[2],  # name
            "ID GetScreen": list(data.values())[0],  # id
            "Дата и время последнего состояние в сети": datetime.datetime.fromtimestamp(list(data.values())[6]).strftime('%Y-%m-%d %H:%M:%S'),
            "IP": list(geo.values())[0],  # ip
            "Страна": list(geo.values())[3],  # country
            "Регион": list(geo.values())[4],  # region
            "Город": list(geo.values())[5],  # city
            "Версия программного агента": list(data.values())[12],  # version
            "Биос": list(hardware.values())[0],  # BIOS
            "Версия биос": list(hardware.values())[2],  # BIOSVersion
            "Процессор": list(hardware.values())[3],  # CPU
            "Количество ядер": list(hardware.values())[4],  # CPUCores
            "Скорость процессора": list(hardware.values())[7],  # CPUSpeed
            "IP/MAC": "\n".join(list(hardware.values())[9]),  # IP_MAC
            "Модель компьютера": list(hardware.values())[10],  # model
            "Имя компьютера": list(hardware.values())[11],  # coputer_name
            "DISKS": disks,  # disks
            "HDD names": hdd_names,  # disks_name
            "Size": size_disks,  # size_disks
            "FreeSpace": freespace_disks,  # free_spase
            "Версия ОС": list(hardware.values())[25],  # os_version
            "Название видеокарты": list(hardware.values())[34],  # videoname
            "Память видеокарты": list(hardware.values())[35],  # videoram
            "ID последнего подключения": last_id(text),
            "Дата старта последнего подключения": last_start(text),
            "Дата окончания последнего подключения": last_stop(text),
            "Количество подключений": last_total(text)
        }
        clients.append(client_dict)



    file = open("data.json", "w")
    json.dump(clients, file, indent=4)
    file.close()
