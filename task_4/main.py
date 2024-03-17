def parse_input(user_input): # Функція для підготовки введеного корисувачем тексту. Розділяє команду та аргументи 
   cmd, *args = user_input.split()
   cmd = cmd.strip().lower()
   return cmd, *args

def add_contact(args, contacts): # Функція для додавання контактів в словник 
    name, phone = args
    contacts[name] = phone
    return "Contact addet"

def change_contact(args, contacts): # Функція для зміни номеру в існуючому контакті контакті 
        name, phone = args
        if name not in contacts:
            raise KeyError(f"Contact with the name {name} was not found.")
        contacts[name] = phone
        return "Contact updated."

def snow_phone(args, contacts): # Функція для виведення номеру по імені контакта 
    *_,phone = args
    value = contacts[phone]
    return value

def main(): # Основна функція для обробки запитів користувача. В ній використовуються інші функції
    try: # блок try-except для обробки помиилок 
        contacts = {}
        print("Welcome to asistant bot")

        while True: #вічний цикл 
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                    print(add_contact(args, contacts))      
            elif command == "phone":
                    print(snow_phone(args, contacts))
            elif command == "change":
                    print(change_contact(args, contacts))
            elif command == "all":
                print(contacts)
            else:
                print("invalid command")
    except KeyError : # перехоплення помилок KeyError
        print(f"Contact with the name {args[0]} was not found.")
    except ValueError as args: # перехоплення помилок ValueError
        print(args)
    
if __name__ == "__main__":
    main()
         
    
