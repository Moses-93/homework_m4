import re

file_path = r"" # абсолютний шлях до файлу

def total_salary(path): # функція яка приймає шлях до файлу 
    try:
        with open(path, "r") as file: # відкриваємо та читаємо файл за допомогою менеджера контексту  
            read = file.read() 
            salery = [int(num) for num in re.findall("\d+", read)]# витягуємо тільки числа 
            full = sum(salery)  # сумуємо ЗП 
            medium = full / len(salery)  # ділимо на кількість робітників 
    except Exception:  # обробляємо вийнятки 
        print("Програма не може розпізнати ваші данні")

        return "Загальна сумма:",full, "Cередня сумма:", medium # повертаємо загальну та середню зп в кортежі 

print(total_salary()) 