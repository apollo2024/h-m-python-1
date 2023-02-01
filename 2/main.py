# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
from random import randint

rand_number = randint(100, 999)

print(rand_number)
print(rand_number % 10 + rand_number % 100 //10 + rand_number // 100)

