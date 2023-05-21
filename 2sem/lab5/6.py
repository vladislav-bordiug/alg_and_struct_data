def exp_filter(measurements, alpha):  # Функция получает измерения и коэффициент сглаживания
    s = [0] * (len(measurements) + 1)
    s[0] = measurements[0]  # Начальное значение возьмем за первое измерение
    for i in range(1, len(s)):
        s[i] = alpha * measurements[i - 1] + (1 - alpha) * s[i - 1]
    return s

measurements = [10, 15, 13, 12, 16, 18, 14, 20, 17, 19]  # Измерения
print('Processed values:',exp_filter(measurements, 0.5))
