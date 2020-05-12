import numpy as np


def game_core_v1(number):
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
    Функция принимает загаданное число и возвращает число попыток
    """
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def game_core_v2(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
    """
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # выход из цикла, если угадали


def game_core_v3(number):
    """Каждый раз находим середину между верхней и нижней границей диапазона,
        в котором находится искомое число - это и будет наш предиктор.
        Если загаданное число меньше предиктора то верхняя граница приравнивается
        к предиктору. Если меньше, то нижняя граница.
    """
    low = 1  # Нижнюю границу устанавливаем вначале равной единице
    top = 100  # Верхнюю соответственно 100. Это известные нам условия задачи
    count = 1  # Счётчки на единицу, т.к. первый предиктор мы считаем вне тела цикла
    predict = top + low // 2  # Сам предиктор считать всегда будем именно так. Округляем в меньшую сторону

    while number != predict:
        count += 1
        predict = (low + top) // 2
        if predict > number:
            top = predict
        elif low < number:
            low = predict
        else:
            break
    return count


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v3)
