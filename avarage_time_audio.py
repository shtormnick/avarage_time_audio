from mutagen.mp3 import MP3
from datetime import datetime
import os, sys


storage = {
    "date": "",
    "path_to_folder": "",
    "sys_name": ""
}

def is_valid_date(date_string, format='%d-%m-%y'):
    try:
        datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False

def input_storage(dict_storage):
    default_path = r'C:\ProScan\Recordings\\'
    date = input(
    'введите дату в формате %дд-%мм-%гг\nоставьте поле пустым, если хотите оставить сегодняшнюю дату\n'
    )
    if date == "":
        date = datetime.now().strftime('%d-%m-%y')
    elif is_valid_date(date) is not True:
        print("вы ввели дату в неправильном формате")
        quit()
    dict_storage["date"] = date

    path_to_folder = input("введите путь к папке с аудиозаписями, например: C:\ProScan\Recordings\\\n")
    if path_to_folder == "":
        path_to_folder = default_path
    dict_storage["path_to_folder"] = path_to_folder
    
    sys_name = input("введите название папки вашей системы\n")
    dict_storage["sys_name"] = sys_name

def dashs(sentence):
    lenght = len(sentence)
    print("-"*lenght)

input_storage(storage)

def user_path(date_p=storage["date"], p_i=storage["path_to_folder"], s_n=storage["sys_name"]):
    path = os.path.join(p_i, date_p, s_n)
    return path
        

def calculate_audio_info(path):
    total_time = 0
    count = 0

    for file in os.listdir(path):
        audio = MP3(path+f"\{file}")
        if file.endswith(".mp3") and audio.info.length >= 1.0:     
            total_time += audio.info.length
            count += 1

    average_time = (total_time / count) / 60

    return average_time, count
    
audio_info = calculate_audio_info(user_path())

print("\nСреднее время аудио за день {:.2f} минут за {}".format(audio_info[0], storage["date"]))
print("\nКоличество аудио за день {} больше 1сек".format(audio_info[1]))
print(sys.stdin.readline())
