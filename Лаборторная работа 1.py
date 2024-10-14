# Лабораторная работа 1.
# Базовый калькулятор

def calculate(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Ошибка: деление на ноль"
    else:
        return "Операция не поддерживается"

def number(prompt):
    while True:
        user_input=input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Вы ввели некорректный символ.Убедитесь, что все значения являются числами.")
# Получение операции от пользователя
operation = input("Введите операцию (+ для сложения, - для вычитания, * для умножения, / для деления): ")

# Получение двух чисел от пользователя
num1 = number("Введите первое число:")
num2 = number("Введите второе число: ")




# Выполнение операции и вывод результата
result = calculate(operation, num1, num2)
print(f"Результат: {result}")