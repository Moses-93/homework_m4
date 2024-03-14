def get_cats_info(path): # ф-кція, яка приймає шлях
    try:
        with open(path, "r",) as file_cats: # відкриваємо файл
            cats = []
            content = file_cats.readlines() #читаємо файл по рядках 
            for cat in content: #ітеруємося по кожному рядку 
                id_, name,age = cat.split(",") #розбиваємо рядок по комах 
                cats.append({"id": id_, "name": name, "age": age.strip()}) #додаємо в список словники з данними 
    except Exception:# оброблюємо вийнятки 
        print("Програма не може розпізнати ваші данні")

    return cats #повертаємо список зі словниками 

 
file_path = r"" # абсолютний шлях до файлу

print(get_cats_info(file_path))
    

