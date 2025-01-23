import random

kisloti = {
    "CI (I)": "хлориды",
    "Br (I)": "бромиды",
    "F (I)": "фториды",
    "I (I)": "иоды",
    "S (II)": "сульфиды",
    "NO₂": "нитрины",
    "NO₃": "нитраты",
    "SO₂ (II)": "сульфиты",
    "SO₄ (IV)": "сульфаты",
    "CO₃ (II)": "карбонаты",
    "PO₄ (III)": "фосфаты",
    "SiO₃ (II)": "силикаты"
}


def guess_elements(balls):
    items = list(kisloti.items())  
    random.shuffle(items) 

    for element, nazv in items:
        while True:
            print(f"Какое название у кис.остатка '{element}'?")
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
        break  
         
