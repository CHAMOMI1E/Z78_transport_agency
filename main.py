class Transport_agency(object):
    EARNINGS = 0


class Car(Transport_agency):
    def __init__(self, distance):
        self.distance = distance

    def set_earnings(self, earnings):
        Transport_agency.EARNINGS += (earnings * 0.2)


class Railway(Transport_agency):
    def __init__(self, distance):
        self.distance = distance

    def set_earnings(self, earnings):
        Transport_agency.EARNINGS += (earnings * 0.2)


class Air_playn(Transport_agency):
    def __init__(self, distance):
        self.distance = distance

    def set_earnings(self, earnings):
        Transport_agency.EARNINGS += (earnings * 0.5)


"""
логика по рекомендации траснортного средства следующая:
если: 
      город-1                город-2          вид транспортного средства
    1(большой)             1(большой)             самолет(рекомендуем)
    1(большой)             2(средний)                   поезд
    1(большой)            3(маленький)                автомобиль
    2(средний)             2(средний)                   поезд
    2(средний)            3(маленький)                автомобиль
    3(маленький)          3(маленький)                автомобиль
"""
i = 1
dicts = {}
while True:
    cargo_weight = int(input("Введите вес груза в кг(1р/кг): "))
    distance = int(input("Введите расстояние для доставки (в км): "))
    large_of_city_output = int(input("Введите размер города отправителя (Большой-1\Средний-2\Маденький-3): "))
    large_of_city_input = int(input("Введите размер города получателя (Большой-1\Средний-2\Маденький-3): "))
    spl = {}
    # система рекомендации транспортного средства для отправления одним рейсом
    # ТС - самолет
    if large_of_city_output == 1 and large_of_city_input == 1:
        print(f"Вид траспорта - САМОЛЕТ - цена 3р/км ")
        summ_for_transport = distance * 3 + cargo_weight  # сумма за всю перевозку
        print(f"ИТОГО: {summ_for_transport}")
        transport = Air_playn(distance)
        transport.set_earnings(summ_for_transport)
        print("Спасибо что выбрали нас!!!")
        # dicts.setdefault(i, f"из {large_of_city_output} города в {large_of_city_input} город, расстояние-{distance}, вес груза-{cargo_weight}")
        dicts[i] = f"из {large_of_city_output} города в {large_of_city_input} город, расстояние-{distance}, вес груза-{cargo_weight}"


    # ТС - поезд
    elif large_of_city_output != 3 and large_of_city_input != 3 and large_of_city_input == 2 or large_of_city_output == 2:
        print(f"Вид траспорта - ПОЕЗД - цена 1р/км ")
        summ_for_transport = distance + cargo_weight  # сумма за всю перевозку
        print(f"ИТОГО: {summ_for_transport}")
        transport = Railway(distance)
        transport.set_earnings(summ_for_transport)
        print("Спасибо что выбрали нас!!!")
        # dicts.setdefault(i, f"из {large_of_city_output} города в {large_of_city_input} город, расстояние-{distance}, вес груза-{cargo_weight}")
        dicts[i] = f"из {large_of_city_output} города в {large_of_city_input} город, расстояние-{distance}, вес груза-{cargo_weight}"

    # ТС - ААААВТОМОБИЛЬ!!!!
    elif large_of_city_output == 3 or large_of_city_input == 3:
        print(f"Вид траспорта - АВТОМОБИЛЬ - цена 2р/км ")
        summ_for_transport = distance * 2 + cargo_weight  # сумма за всю перевозку
        print(f"ИТОГО: {summ_for_transport}")
        transport = Railway(distance)
        transport.set_earnings(summ_for_transport)
        print("Спасибо что выбрали нас!!!")
        # dicts.setdefault(i, f"из {large_of_city_output} города в {large_of_city_input} город, расстояние-{distance}, вес груза-{cargo_weight}")
        dicts[i] = f"из {large_of_city_output} города в {large_of_city_input} город, расстояние-{distance}, вес груза-{cargo_weight}"

    # системное меню, что бы его вызвать нужно вписать в размер города 99(в оба)!!!!
    elif large_of_city_output == 99 and large_of_city_input == 99:
        admin = Transport_agency()
        print(f"ADMIN: {Transport_agency.EARNINGS} - доход")
        print(dicts)
        i -= 1

    else:
        break

    i += 1
