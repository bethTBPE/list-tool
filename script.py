def add_item(items, item):
    items.append(item)
    return items
def remove_item(items, item):
    if item in items:
        items.remove(item)
    else:
        print("Елемент не знайдено!")
    return items
def search_item(items, item):
    return item in items

my_list = []

while True:
    print("\nМеню:")
    print("1 — Додати елемент")
    print("2 — Видалити елемент")
    print("3 — Знайти елемент")
    print("4 — Показати список")
    print("5 — Вийти")

    choice = input("Виберіть дію: ")

    if choice == "1":
        item = input("Введіть елемент: ")
        my_list = add_item(my_list, item)

    elif choice == "2":
        item = input("Введіть елемент для видалення: ")
        my_list = remove_item(my_list, item)

    elif choice == "3":
        item = input("Введіть елемент для пошуку: ")
        if search_item(my_list, item):
            print("Елемент знайдено!")
        else:
            print("Елемент відсутній.")

    elif choice == "4":
        print("Поточний список:", my_list)

    elif choice == "5":
        print("Вихід...")
        break

    else:
        print("Невірний вибір, спробуйте ще раз.")