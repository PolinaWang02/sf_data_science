"""Игра угадай число
Компьютер угадывает число за минимальное количество попыток
"""

import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """    
    
    count = 0
    predict = np.random.randint(1, 101)
    
    while number%10 != predict%10:
        count += 1
        if number//10 > predict//10:
            predict += 10
        elif number//10 < predict//10:
            predict -= 10
        elif number//10 == predict//10:
            if number%10 > predict%10:
                predict += 1
            elif number%10 < predict%10:
                predict -= 1

    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
