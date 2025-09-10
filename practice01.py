# Kalkulyator dasturi

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Xatolik! Nolga bo‘lish mumkin emas."

print("Kalkulyator: +, -, *, / amallarni bajaradi.")

a = float(input("1-sonni kiriting: "))
b = float(input("2-sonni kiriting: "))
operation = input("Amalni tanlang (+, -, *, /): ")

if operation == "+":
    print("Natija:", add(a, b))
elif operation == "-":
    print("Natija:", subtract(a, b))
elif operation == "*":
    print("Natija:", multiply(a, b))
elif operation == "/":
    print("Natija:", divide(a, b))
else:
    print("Xato amal kiritildi!")
