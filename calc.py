import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Декоратор с использованием замыкания (closure)
def log_decorator(func):
    def wrapper(*args, **kwargs):
        operand1, operand2, action = args
        logging.info(f"Входные значения: operand1 = {operand1}, operand2 = {operand2}, действие = '{action}'")

        # Вызов декорируемой функции calculate и получение результата
        result = func(*args, **kwargs)

        # Логирование результата
        logging.info(f"Результат выполнения: {result}")

        return result
    return wrapper

# Декорирование функции calculate с использованием @-синтаксиса
@log_decorator
def calculate(a, b, operation):
    operations = {
        "+": (lambda a, b: a + b),
        "-": (lambda a, b: a - b),
        "*": (lambda a, b: a * b),
        "/": (lambda a, b: a / b if b != 0 else "Ошибка: деление на ноль")
    }
    try:
        return operations[operation](a, b)
    except KeyError:
        return "Ошибка: неизвестная операция"

# Тестирование функции
def main():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    operation = input("Введите операцию (+, -, *, /): ")
    result = calculate(a, b, operation)
    print(f"Результат: {result}")

if __name__ == '__main__':
    main()
