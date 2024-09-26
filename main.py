import datetime
import handler
import google_sheet_handler as g
import warnings_new as w


if __name__ == "__main__":
    handler.handl()
    print("Парсинг прошел успешно")
    if w.handler_memory(w.read_json("data.json")) != "0":
        addr_to = "support@meridiant.ru"
        w.send_email(addr_to, "Критический уровень памяти на модуле управления клиента!",
                     w.handler_memory(w.read_json("data.json")))
        addr_to2 = "helpme.meridian@gmail.com"  # Получатель
        w.send_email(addr_to2, "Критический уровень памяти на модуле управления клиента!",
                     w.handler_memory(w.read_json("data.json")))
        addr_to3 = 'alial@mrdn.support'
        w.send_email(addr_to3, "Критический уровень памяти на модуле управления клиента!",
                     w.handler_memory(w.read_json("data.json")))

        t = g.Table()
        t.clear_table()
        t.handle_json_for_table()


