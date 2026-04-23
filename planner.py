records = []  

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
        elif choice in ["1", "2", "3", "4"]:
            print("⏳ Функция будет добавлена позже.")
        else:
            print("❌ Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()