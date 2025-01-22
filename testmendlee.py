import random



elements = {
    'Азот': ('N', 'Эн'),
    'Алюминий': ('A1', 'Алюминий'),
    'Барий': ('Ba', 'Барий'),
    'Бром': ('Br', 'Бром'),
    'Водород': ('H', 'Аш'),
    'Железо': ('Fe', 'Феррум'),
    'Иод': ('I', 'Иод'),
    'Калий': ('K', 'Калий'),
    'Кальций': ('Ca', 'Кальций'),
    'Кислород': ('O', 'О'),
    'Кремний': ('Si', 'Силициум'),
    'Магний': ('Mg', 'Магний'),
    'Медь': ('Cu', 'Купрум'),
    'Натрий': ('Na', 'Натрий'),
    'Ртуть': ('Hg', 'Гидраргиум'),
    'Свинец': ('Pb', 'Плюмбум'),
    'Сера': ('S', 'Эс'),
    'Серебро': ('Ag', 'Аргентум'),
    'Углерод': ('C', 'Це'),
    'Фосфор': ('P', 'Пэ'),
    'Фтор': ('F', 'Фтор'),
    'Хлор': ('C1', 'Хлор'),
    'Цинк': ('Zn', 'Цинк')
}

def guess_elements(balls):
    items = list(elements.items())  
    random.shuffle(items) 

    for element, (simbol, proiz) in items:
        while True:
            print(f"Какой символ у элемента '{element}'?")
            answer = input("Введите ваш ответ (символ и произношение через пробел): ").strip()

            if answer.lower() == f"{simbol.lower()} {proiz.lower()}":
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

        if total_balls >= 23:
            print("\nСпасибо за игру! У вас всего", total_balls, "баллов. Оценка: 5")
        elif total_balls >= 20:
            print("Спасибо за игру! У вас всего", total_balls, "баллов. Оценка: 4")
        elif total_balls >= 15:
            print("Спасибо за игру! У вас всего", total_balls, "баллов. Оценка: 3")
        else:
            print("Спасибо за игру! У вас всего", total_balls, "баллов. Оценка: 2")
        break  
         

                

    
