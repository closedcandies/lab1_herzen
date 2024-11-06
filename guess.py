def binary_search(floor, ceil, value):
  operations = 1
  middle = (floor + ceil) // 2
  while middle != value:
    operations += 1
    if middle < value:
      floor = middle
    elif middle > value:
      ceil = middle
    middle = (floor + ceil) // 2

  return operations


def main():
  value = int(input("Число, которое необходимо угадать:"))
  floor = int(input("Нижняя граница диапазона:"))
  ceil = int(input("Верхняя граница диапазона:"))

  print("Число отгадано. Количество сравнений:",               binary_search(floor, ceil, value))


if __name__ == '__main__':
  main()