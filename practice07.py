
def check_answer(user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
        return True
    else:
        return False

def ask_question(question: str, correct_answer: str):
    user_answer = input(question + " → ")
    if check_answer(user_answer, correct_answer):
        print(" To‘g‘ri javob!")
    else:
        print(" Noto‘g‘ri! To‘g‘ri javob:", correct_answer)


print("Mini Quiz Game boshladik! \n")

ask_question("1. O‘zbekistonning poytaxti qaysi?", "Toshkent")
ask_question("2. Python dasturlash tilida 'matn' qanday yoziladi? (int/str/float)", "str")
