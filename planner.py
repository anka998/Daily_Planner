records = [] 

def add_record():
    print("\n--- Добавление записи ---")
    date = input("Введите дату (ГГГГ-ММ-ДД): ")
    text = input("Введите текст записи: ")
    records.append({"date": date, "text": text})
    print(f"✅ Запись на {date} добавлена!\n") 

def show_menu():
    print("=" * 35)
    print("📅  Е Ж Е Д Н Е В Н И К")
    print("=" * 35)
    print("1. Добавить запись")
    print("2. Показать все записи")
    print("3. Найти запись по дате")
    print("4. Удалить запись")
    print("0. Выход")
    print("=" * 35)

def main():
    while True:
        show_menu()
        choice = input("Выберите действие (0-4): ")
        
        if choice == "0":
            print("До свидания!")
            break
        elif choice == "1":
            add_record()
        elif choice in ["2", "3", "4"]:
            print("⏳ Функция будет добавлена позже.")

if __name__ == "__main__":
    main()