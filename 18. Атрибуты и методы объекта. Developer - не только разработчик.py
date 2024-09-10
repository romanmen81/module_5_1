class House:
    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов объекта
        self.name = name  # Имя
        self.number_of_floors = number_of_floors  # Количество этажей

    def go_to(self, new_floor):
        # Метод для перехода на указанный этаж
        if new_floor < 1 or new_floor > self.number_of_floors:
            # Если этаж вне допустимых границ
            print("Такого этажа не существует")
        else:
            # Если этаж находится в допустимых границах, выводим все этажи до него
            for floor in range(1, new_floor + 1):
                print(floor)

# Создаем объект класса House с произвольными параметрами
h1 = House('ЖК Эльбрус', 18)
h2 = House('Домик в деревне', 2)

# Вызываем метод go_to у созданных объектов с произвольными номерами этажей
h1.go_to(5)  # Ожидается вывод этажей 1-5
h2.go_to(10) # Ожидается вывод "Такого этажа не существует"