def total_salary(path): # функція яка приймає шлях до файлу 
    try: 
        salaries = []  # список для зберігання зарплат
        with open(path, "r", encoding="utf-8") as file: # відкриваємо та читаємо файл за допомогою менеджера контексту  
            for read in file.readlines(): # Перебирааємо файл з зп та зберігаємо данні
                _, salary = read.split(",") #розділяємо по ","
                salaries.append(int(salary))  # додаємо зарплату до списку

        full = sum(salaries)  # сумуємо ЗП 
        medium = full / len(salaries)  # ділимо на кількість робітників 
    except ValueError as error:
        print(error)
    return "Загальна сумма:", full, "Cередня сумма:", medium # повертаємо загальну та середню зп 

file_path = r"" # абсолютний шлях до файлу

print(total_salary(file_path))  
