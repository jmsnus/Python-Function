# Yosh hisoblovchi dastur

def calculate_age(birth_year, current_year):
    return current_year - birth_year

birth_year = int(input("Tug‘ilgan yilingizni kiriting: "))
current_year = int(input("Hozirgi yilni kiriting: "))

age = calculate_age(birth_year, current_year)
print("Sizning yoshingiz:", age)

if age >= 18:
    print("Siz 18 yoshsiz")
else:
    print("Siz 18 ga to'lmagansiz")
