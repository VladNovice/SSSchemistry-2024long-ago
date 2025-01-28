import random

kisloti = {
    "Hce": "соляная",
    "HBr": "бромоводородная",
    "HF": "фтороводородная",
    "HI": "иодоводородная",
    "H₂S": "сероводородная",
    "HNO₂": "азотистая",
    "HNO₃": "азотная",
    "H₂SO₃": "серистая",
    "H₂SO₄": "серная",
    "H₂CO₃": "угольная",
    "H₂PO₄": "фосфорная",
    "H₂SiO₃": "кремневая"
}


def guess_elements(balls):
    items = list(kisloti.items())  
    random.shuffle(items) 

    for element, nazv in items:
        while True:
            print(f"Какое название у кислоты '{element}'?")
            answer = input("Введите ваш ответ: ").strip()

            if answer.lower() == f"{nazv}":
                balls += 1
                print("Молодец! У тебя", balls, "баллов.")
                break 
            else:
                balls -= 1
                print("Попробуй еще раз. -1 Балл,", " Всего ", balls)

    return balls  

if __name__ == "__main__":
    total_balls = 0 
    while True:
        total_balls = guess_elements(total_balls)  

        if total_balls >= 11:
            print("\nСпасибо за игру! У вас всего", total_balls, "баллов. Оценка: 5")
        elif total_balls >= 10:
            print("Спасибо за игру! У вас всего", total_balls, "баллов. Оценка: 4")
        elif total_balls >= 8:
            print("Спасибо за игру! У вас всего", total_balls, "баллов. Оценка: 3")
        else:
            print("Спасибо за игру! У вас всего", total_balls, "баллов. Оценка: 2")

        alNswer = input("Хотите попробывать еще раз?: ")
        if alNswer == "ДА":
            total_balls = 0, guess_elements()
        else:
            break
         