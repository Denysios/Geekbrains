# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

n = input('Введите число от 1 до 9 включительно: ')
# Способ 1 (последовательный способ)
# nn = n + n
# nnn = n + n + n
# result = int(n) + int(nn) + int(nnn)
# print(result)

# Способ 2 (Пока читал методичку нашел еще этот способ, более удобный)
result = int(n) + int(n*2) + int(n*3)
print(result)