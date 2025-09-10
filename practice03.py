# Juft/Toq son tekshiruvchi dastur


def is_even(number):
    return number % 2 == 0


def print_even_message(number):
    if is_even(number):
        print(number, "→ Juft son ")
    else:
        print(number, "→ Toq son ")


num = int(input("Son kiriting: "))
print_even_message(num)
