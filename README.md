# Інструмент списків
Програма яка допомагає спростити роботу зі списками

## Опис
Цей проєкт представляє собою інструмент для роботи зі списками з текстовим інтерфейсом, який дозволяє виконувати основні функції в інтерактивному режимі.

## Функціональність
- Додавання елементу до списку
- Видалення елементу зі списку
- Знаходження елементу у списку

## Вимоги
- Python 3.7 або вищ
- Операційна система: Windows, macOS, Linux

## Встановлення
1. Клонуйте репозиторій:
``````bash
git clone https://github.com/ваше-ім’я/calculator-project.git
``````
2. Перейдіть у папку проєкту:
``````bash
cd calculator-project
``````
3. Запустіть програму:
``````bash
python calculator.py
``````
## Використання
``````
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
``````

## Автор
**Ім’я**: Єлизавета Олександрівна
**Група**: КН-21
**Email**: beth.tbpe@gmail.com
**GitHub**: [@bethTBPE](https://github.com/bethTBPE)