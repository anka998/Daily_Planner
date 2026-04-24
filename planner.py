# Приложение "ЕЖЕДНЕВНИК"

records = []

def add_record():
    print("\n--- Добавление записи ---")
    date = input("Введите дату (ГГГГ-ММ-ДД): ")
    text = input("Введите текст записи: ")
    records.append({"date": date, "text": text})
    print(f"Запись на {date} добавлена!\n")

def view_records():
    print("\n--- Все записи ---")
    if not records:
        print("Записей нет.")
    else:
        for i, rec in enumerate(records):
            print(f"{i+1}. {rec['date']} — {rec['text']}")
    print()

def search_record():
    print("\n--- Поиск записи ---")
    date = input("Введите дату для поиска (ГГГГ-ММ-ДД): ")
    found = False
    for rec in records:
        if rec["date"] == date:
            print(f"Найдено: {rec['date']} — {rec['text']}")
            found = True
    if not found:
        print(f"Записей на {date} не найдено.")
    print() 
def delete_record():
    print("\n--- Удаление записи ---")
    view_records()
    if records:
        try:
            num = int(input("Введите номер записи для удаления: "))
            if 1 <= num <= len(records):
                removed = records.pop(num - 1)
                print(f"Запись '{removed['text']}' удалена!")
            else:
                print("Неверный номер записи.")
        except ValueError:
            print("Введите число.")
    print() 
def show_menu():
    print("=" * 35)
    print("Е Ж Е Д Н Е В Н И К")
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
        elif choice == "2":
            view_records()
        elif choice == "3":
            search_record()
        elif choice == "4":
            delete_record()
        else:
            print("Неверный ввод. Попробуйте снова.") 
if __name__ == "__main__":
    main() 
