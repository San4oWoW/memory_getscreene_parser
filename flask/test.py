import datetime
import json



with open('data.json', 'r', encoding='utf-8') as f:
    text = json.load(f)
    client_dict = {}

    data = text[0]["data"]
    key_id = list(data.keys())[0]
    value_id = list(data.values())[0]


    name = text[0]["data"]
    key_name = list(name.keys())[1]
    value_name = list(name.values())[1]

    last_time = text[0]["data"]
    last_time_value = datetime.datetime.fromtimestamp(list(last_time.values())[6])
    print(list(last_time.keys())[6])
    print(last_time_value.strftime('%Y-%m-%d %H:%M:%S'))

    geo_ip = text[0]["data"]["geo"]
    print(list(geo_ip.keys())[0])
    print(list(geo_ip.values())[0])

    country = text[0]["data"]["geo"]
    print(list(country.keys())[3])
    print(list(country.values())[3])

    region = text[0]["data"]["geo"]
    print(list(region.keys())[4])
    print(list(region.values())[4])

    city = text[0]["data"]["geo"]
    print(list(city.keys())[5])
    print(list(city.values())[5])

    version = text[0]["data"]
    print(list(version.keys())[12])
    print(list(version.values())[12])

    online = text[0]["data"]
    print(list(online.keys())[13])
    print(list(online.values())[13])

    BIOS = text[0]["data"]["hardware"]
    print(list(BIOS.keys())[0])
    print(list(BIOS.values())[0])

    BIOS_version = text[0]["data"]["hardware"]
    print(list(BIOS_version.keys())[2])
    print(list(BIOS_version.values())[2])

    CPU = text[0]["data"]["hardware"]
    print(list(BIOS_version.keys())[3])
    print(list(BIOS_version.values())[3])

    CPU_cores = text[0]["data"]["hardware"]
    print(list(CPU_cores.keys())[4])
    print(list(CPU_cores.values())[4])

    CPU_speed = text[0]["data"]["hardware"]
    print(list(CPU_speed.keys())[7])
    print(list(CPU_speed.values())[7])

    IP = text[0]["data"]["hardware"]
    print(list(CPU_speed.keys())[9])
    print("\n".join(list(CPU_speed.values())[9]))

    model = text[0]["data"]["hardware"]
    print(list(model.keys())[10])
    print(list(CPU_speed.values())[10])

    computer_name = text[0]["data"]["hardware"]
    print(list(computer_name.keys())[11])
    print(list(computer_name.values())[11])

    HDD_disks = text[0]["data"]["hardware"]["LogicalDisks"]
    disks = ""
    for i in HDD_disks:
        disks += f"{list(i.keys())[0]} {list(i.values())[0]}\n"

    print(disks)

    HDD_name = text[0]["data"]["hardware"]["HDD"]
    hdd_names = ''
    for i in HDD_name:
        hdd_names += f"{list(i.values())[0]}\n"
    print(hdd_names)

    size = text[0]["data"]["hardware"]["LogicalDisks"]
    size_disks = ''
    for i in size:
        size_disks += f"{list(i.keys())[4]}: {list(i.values())[4]}\n"
    print(size_disks)

    freespace = text[0]["data"]["hardware"]["LogicalDisks"]
    freespace_disks = ''
    for i in freespace:
        freespace_disks += f"{list(i.keys())[2]}: {list(i.values())[2]}\n"
    print(freespace_disks)

    os_version = text[0]["data"]["hardware"]
    print(list(os_version.keys())[25])
    print(list(os_version.values())[25])

    video_name = text[0]["data"]["hardware"]
    print(list(video_name.keys())[34])
    print(list(video_name.values())[34])

    video_ram = text[0]["data"]["hardware"]
    print(list(video_name.keys())[35])
    print(list(video_name.values())[35])

    sessions_last_id = text[1]["data"]["sessions"]["last"]
    print(list(sessions_last_id.keys())[0])
    print(list(sessions_last_id.values())[0])

    sessions_last_start = text[1]["data"]["sessions"]["last"]
    print(list(sessions_last_start.keys())[1])
    print(list(sessions_last_start.values())[1])

    sessions_last_stop = text[1]["data"]["sessions"]["last"]
    print(list(sessions_last_stop.keys())[1])
    print(list(sessions_last_stop.values())[1])

    sessions_last_total = text[0]["data"]["sessions"]["total"]
    print(sessions_last_total)
    # print(list(sessions_last_total.keys()))
    # print(list(sessions_last_total.values()))






















