# Sirli son o‘yini 

def check_guess(secret, guess):
    if secret == guess:
        return True
    else:
        return False

def print_result(is_correct):
    if is_correct:
        print("To‘g‘ri topdingiz!")
    else:
        print(" Xato, yana urinib ko‘ring.")


secret_number = 5   
print("Men 1 dan 10 gacha bo‘lgan son o‘yladim. Topishga harakat qiling!")

guess = int(input("Son kiriting: "))

result = check_guess(secret_number, guess)
print_result(result)
