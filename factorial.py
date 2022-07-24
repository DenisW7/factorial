#программа вычисляющая фкториал числа

number = int(input())
factorial = 1
for i in range(factorial, number + 1):
	factorial *= i
	
print(factorial)