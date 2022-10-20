value_one = int(input("Введіть перше число: "))

operation = input("Виберіть дію: + - * /: ")

value_two = int(input("Введіть друге число: "))

if operation == "+":
    print(f"Сума: {value_one + value_two}")
if operation == "-":
    print(f"Різниця: {value_one - value_two}")
if operation == "*":
    print(f"Добуток: {value_one * value_two}")
if operation == "/":
    if value_two == 0:
        print("ERROR! На нуль ділити неможна!")
        quit()

        print(f"Частка: {value_one / value_two}")