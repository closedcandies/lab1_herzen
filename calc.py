def test_basic():
  assert calculate(5, 10, "+") == 15


def test_negative():
  assert calculate(-10, -4, "*") == 40


def test_float():
  assert calculate(6.8, 10.8, "+") == 17.6


def test_absurd():
  assert calculate("dog", "cat", "good") == "ABSURD"


def calculate(a, b, operation):
  operations = {"+": (lambda a, b: a + b),
               "-": (lambda a, b: a - b),
               "*": (lambda a, b: a * b),
               "/": (lambda a, b: a / b)}
  try:
    return operations[operation](a, b)
  except ZeroDivisionError:
    return "DIVISION BY ZERO"
  except Exception as e:
    return "ABSURD"


def main():
  a = float(input("Первое число:"))
  b = float(input("Второе число:"))
  operation = input("Операция:")
  print(calculate(a, b, operation))


def testing():
  test_basic()
  test_negative()
  test_float()
  test_absurd()


if __name__ == '__main__':
  testing()
  main()