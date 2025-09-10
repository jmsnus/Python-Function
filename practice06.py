# Telefon raqam tekshiruvchi dastur

def is_valid_phone_number(phone: str):
    if len(phone) == 9 and phone.isdigit():
        return True
    else:
        return False


phone = input("Telefon raqamni kiriting : ")

if is_valid_phone_number(phone):
    print(" Telefon raqam to‘g‘ri!")
else:
    print(" Xato! Telefon raqam 9 ta raqamdan iborat bo‘lishi kerak.")
