def PI():
    i = 0
    denominator = 3
    numberGregory = 0
    while i < 499:
        if i % 2 == 0:
            numberGregory = - (1 / denominator) + numberGregory
        else:
            numberGregory = (1 / denominator) + numberGregory
        denominator += 2
        i += 1
    else:
        numberGregory = numberGregory + 1
        print("Результат работы ф-лы: ", "%f" % numberGregory)

def DefinitionQuantity():
    VowelsList = "AEIOUaeiouАЕИОУаеиоуЁёЫыЭэЮюЯя"
    QuantityVowels = 0
    QuantityConsonants = 0
    mas = []
    text = input("Введите строку: ")
    for char in text:
        if char.isalpha() == True:
            if char in VowelsList:
                QuantityVowels += 1
                mas.append(char)
            else:
                QuantityConsonants += 1
    print("Кол-во гласных букв в слове ", text, ": ", QuantityVowels)
    print("Кол-во согласных букв в слове ", text, ": ", QuantityConsonants)
    if QuantityVowels == QuantityConsonants:
        if QuantityVowels != 0:
            print("Гласные буквы в ", text, ": ", ' '.join(mas))
        else:
            print("Гласных букв нету")
def Mas():
    my_list = [1, 34, 'qwerty', 12, 13, 16, 'Love', 'Python']
    numbers_list = []
    words_list = []
    product_numbers = 1
    for item in my_list:
        if isinstance(item, int):
            numbers_list.append(item)
        elif isinstance(item, str):
            words_list.append(item)
    sum_numbers = sum(numbers_list)
    for number in numbers_list:
        product_numbers *= number
    print("Список чисел:", numbers_list)
    print("Список слов:", words_list)
    print("Сумма чисел:", sum_numbers)
    print("Произведение чисел:", product_numbers)
    top_three_numbers = []
    for _ in range(3):
        max_number = max(numbers_list)
        top_three_numbers.append(max_number)
        numbers_list.remove(max_number)
    print("Три наибольших элемента:", top_three_numbers)
def Dictionary():
    text = 'An apple a day keeps the doctor away'
    char_count = {}
    for char in text:
        if char.isalpha() == True:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    print(char_count)
def motorcade():
    my_tuple = (3, 7, 1, 5, 11, 9, 23, 67)
    min_even = None
    first_element = my_tuple[0]
    for number in my_tuple:
        if number % 2 == 0:
            if min_even is None or number < min_even:
                min_even = number
    if min_even is not None:
        print("Наименьший четный элемент:", min_even)
    else:
        print("Нет четных элементов, выводим первый элемент:", first_element)
def ShopAutoParts():
    # Создаем словарь с информацией о продукции
    products = {
        "Колодки": ["металл, резина", 1000, 50],
        "Масло моторное": ["масло, синтетика", 500, 30],
        "Фильтр воздушный": ["фильтр, пластик", 300, 40],
    }
    while True:
        print("Меню:")
        print("1. Просмотр описания")
        print("2. Просмотр цены")
        print("3. Просмотр количества")
        print("4. Всю информацию")
        print("5. Покупка")
        print("n. Выход")
        choice = input("Введите номер пункта меню: ")
        if choice == "1":
            product_name = input("Введите название продукции: ")
            if product_name in products:
                print(f"Описание продукции '{product_name}': {products[product_name][0]}")
            else:
                print(f"Продукт '{product_name}' не найден в магазине.")
        elif choice == "2":
            product_name = input("Введите название продукции: ")
            if product_name in products:
                print(f"Цена продукции '{product_name}': {products[product_name][1]} руб.")
            else:
                print(f"Продукт '{product_name}' не найден в магазине.")
        elif choice == "3":
            product_name = input("Введите название продукции: ")
            if product_name in products:
                print(f"Количество продукции '{product_name}' в магазине: {products[product_name][2]} шт.")
            else:
                print(f"Продукт '{product_name}' не найден в магазине.")
        elif choice == "4":
            for product_name in products:
                print(f"Название продукции: {product_name}")
                print(f"Состав: {products[product_name][0]}")
                print(f"Цена: {products[product_name][1]} руб.")
                print(f"Количество: {products[product_name][2]} шт.")
                print()
        elif choice == "5":
            total_price = 0
            while True:
                product_name = input("Введите название продукции для покупки (n - завершить покупку): ")
                if product_name == "n":
                    break
                if product_name in products:
                    quantity = int(input(f"Введите количество продукции '{product_name}': "))
                    if quantity <= products[product_name][2]:
                        products[product_name][2] -= quantity
                        total_price += products[product_name][1] * quantity
                    else:
                        print(f"Недостаточно продукции '{product_name}' в магазине.")
                else:
                    print(f"Продукт '{product_name}' не найден в магазине.")
            print(f"Сумма покупки: {total_price} руб.")
        elif choice == "n":
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите пункт меню снова.")

if __name__ == "__main__":
    while True:
        print("Главное меню:")
        print("1. Вычисление числа Пи (метод Грегори)")
        print("2. Определение количества гласных и согласных букв в строке")
        print("3. Обработка списка чисел и слов")
        print("4. Создание словаря с подсчетом букв в строке")
        print("5. Поиск наименьшего четного элемента в кортеже")
        print("6. Магазин автозапчастей")
        print("7. Выход")
        main_choice = input("Выберите опцию: ")
        if main_choice == "1":
            PI()
        elif main_choice == "2":
            DefinitionQuantity()
        elif main_choice == "3":
            Mas()
        elif main_choice == "4":
            Dictionary()
        elif main_choice == "5":
            motorcade()
        elif main_choice == "6":
            ShopAutoParts()
        elif main_choice == "7":
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите опцию снова.")