from pywebio.input import input, TEXT
from pywebio.output import put_text, put_success, put_error
from pywebio import start_server


def school_quiz():
    # запит ім'я
    user_name = input("Введіть ваше ім'я:", type=TEXT)

    # питання та відповідь
    questions = [
        ("Яка планета є найбільшою у Сонячній системі?", "Юпітер"),
        ("Скільки континентів на Землі?", "7"),
        ("Як називається столиця Франції?", "Париж"),
        ("Який метал є основним у виробництві алюмінієвої фольги?", "Алюміній"),
        ("Скільки кольорів у веселці?", "7"),
    ]

    # скільки правильних
    correct_answers = 0

    # всі
    for question, correct_answer in questions:
        user_answer = input(question, type=TEXT).strip().capitalize()
        if user_answer == correct_answer:
            put_success("Правильно!")
            correct_answers += 1
        else:
            put_error(f"Неправильно! Правильна відповідь: {correct_answer}")

    # результат
    total_questions = len(questions)
    put_text(f"{user_name}, ви відповіли правильно на {correct_answers} із {total_questions} питань.")
    put_text(f"Ваша точність: {correct_answers / total_questions * 100:.2f}%")


# запуск
if __name__ == "__main__":
    start_server(school_quiz, port=8080, debug=True)
