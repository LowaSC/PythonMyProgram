print("В этой программе будет найдена сумма всех чисел меньше 1000, кратных 3 или 5.")

# Объявление переменной, в которой будет вычисляться сумма
sum = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print("Сумма = " + str(sum))
