import json
import smtplib                                              # Импортируем библиотеку по работе с SMTP
import os                                                   # Функции для работы с операционной системой, не зависящие от используемой операционной системы

# Добавляем необходимые подклассы - MIME-типы
import mimetypes                                            # Импорт класса для обработки неизвестных MIME-типов, базирующихся на расширении файла
from email import encoders                                  # Импортируем энкодер
from email.mime.base import MIMEBase                        # Общий тип
from email.mime.text import MIMEText                        # Текст/HTML
from email.mime.image import MIMEImage                      # Изображения
from email.mime.audio import MIMEAudio                      # Аудио
from email.mime.multipart import MIMEMultipart              # Многокомпонентный объект
import gspread

gc = gspread.service_account(filename=os.path.abspath("credentials.json"))
sh = gc.open_by_key("1eHOQcO2Wr6GDohcv9BuogsJequ0M6v1M9eaUI0ys59c")
worksheet = sh.sheet1

def send_email_with_file(addr_to, msg_subj, msg_text, files):
    addr_from = "helpme.meridian@gmail.com"                         # Отправитель
    password  = "xubhdbdubpixbgzr"                                  # Пароль

    msg = MIMEMultipart()                                   # Создаем сообщение
    msg['From']    = addr_from                              # Адресат
    msg['To']      = addr_to                                # Получатель
    msg['Subject'] = msg_subj                               # Тема сообщения

    body = msg_text                                         # Текст сообщения
    msg.attach(MIMEText(body, 'plain'))                     # Добавляем в сообщение текст

    process_attachement(msg, files)

    #======== Этот блок настраивается для каждого почтового провайдера отдельно ===============================================
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    #server.set_debuglevel(True)                            # Включаем режим отладки, если не нужен - можно закомментировать
    server.login(addr_from, password)                       # Получаем доступ
    server.send_message(msg)                                # Отправляем сообщение
    server.quit()                                           # Выходим
    #==========================================================================================================================

def send_email(addr_to, msg_subj, msg_text):
    addr_from = "helpme.meridian@gmail.com"                         # Отправитель
    password  = "adwfykxobyphxtwl"                                  # Пароль

    msg = MIMEMultipart()                                   # Создаем сообщение
    msg['From']    = addr_from                              # Адресат
    msg['To']      = addr_to                                # Получатель
    msg['Subject'] = msg_subj                               # Тема сообщения

    body = msg_text                                         # Текст сообщения
    msg.attach(MIMEText(body, 'plain'))                     # Добавляем в сообщение текст


    #======== Этот блок настраивается для каждого почтового провайдера отдельно ===============================================
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    #server.set_debuglevel(True)                            # Включаем режим отладки, если не нужен - можно закомментировать
    server.login(addr_from, password)                       # Получаем доступ
    server.send_message(msg)                                # Отправляем сообщение
    server.quit()                                           # Выходим

def process_attachement(msg, files):                        # Функция по обработке списка, добавляемых к сообщению файлов
    for f in files:
        if os.path.isfile(f):                               # Если файл существует
            attach_file(msg,f)                              # Добавляем файл к сообщению
        elif os.path.exists(f):                             # Если путь не файл и существует, значит - папка
            dir = os.listdir(f)                             # Получаем список файлов в папке
            for file in dir:                                # Перебираем все файлы и...
                attach_file(msg,f+"/"+file)                 # ...добавляем каждый файл к сообщению

def attach_file(msg, filepath):                             # Функция по добавлению конкретного файла к сообщению
    filename = os.path.basename(filepath)                   # Получаем только имя файла
    ctype, encoding = mimetypes.guess_type(filepath)        # Определяем тип файла на основе его расширения
    if ctype is None or encoding is not None:               # Если тип файла не определяется
        ctype = 'application/octet-stream'                  # Будем использовать общий тип
    maintype, subtype = ctype.split('/', 1)                 # Получаем тип и подтип
    if maintype == 'text':                                  # Если текстовый файл
        with open(filepath) as fp:                          # Открываем файл для чтения
            file = MIMEText(fp.read(), _subtype=subtype)    # Используем тип MIMEText
            fp.close()                                      # После использования файл обязательно нужно закрыть
    elif maintype == 'image':                               # Если изображение
        with open(filepath, 'rb') as fp:
            file = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
    elif maintype == 'audio':                               # Если аудио
        with open(filepath, 'rb') as fp:
            file = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
    else:                                                   # Неизвестный тип файла
        with open(filepath, 'rb') as fp:
            file = MIMEBase(maintype, subtype)              # Используем общий MIME-тип
            file.set_payload(fp.read())                     # Добавляем содержимое общего типа (полезную нагрузку)
            fp.close()
            encoders.encode_base64(file)                    # Содержимое должно кодироваться как Base64
    file.add_header('Content-Disposition', 'attachment', filename=filename) # Добавляем заголовки
    msg.attach(file)                                        # Присоединяем файл к сообщению


def read_json(name: str):
    with open(name, 'r', encoding='utf-8') as f:
        return json.load(f)


def check_memory(free_memory: list, size: list) -> bool:
    choice = False
    for i in range(len(free_memory)):
        if int(free_memory[i]) <= 15000 and int(free_memory[i]) != 0 and int(size[i]) > 100000 and int(size[i]) != 0:
            choice = True
    return choice


def handler_memory(file: str) -> str:
    result = "У клиентов:\n"
    count = 0
    for i in file:
        name = i["Имя клиента"]
        mas = i["FreeSpace"].split("\n")
        size = i["Size"].split("\n")
        mas.pop(-1)
        size.pop(-1)
        if check_memory(mas, size):
            result += f"{name}\n"
            count += 1
    if count >= 1:
        result += "Критический уровень памяти(менее 15 гб), свяжитесь для решения!"
        return result
    else:
        return "0"
#print(handler_memory(read_json("data.json")))
# # Использование функции send_email()
# addr_to   = "support@meridiant.ru"                                # Получатель
#                               # Список файлов, если вложений нет, то files=[]                        # Если нужно отправить все файлы из заданной папки, нужно указать её
# send_email(addr_to, "Критический уровень памяти на модуле управления клиента!", handler_memory(read_json("data/")))
#
# addr_to2   = "helpme.meridian@gmail.com"                                # Получатель
# send_email(addr_to2, "Критический уровень памяти на модуле управления клиента!", client_names_sort())