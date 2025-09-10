

def get_grade(score):
    score = int(score)
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "c"
    else:
        return "F"
   

ball = input("Balingizni kiriting: ")
baho = get_grade(ball)
print("Sizning bahoyingiz:", baho)