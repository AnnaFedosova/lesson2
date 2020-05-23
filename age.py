your_age=int(input("Сколько вам лет?"))

# определяем, чем пользователь занимается, исходя из возраста
def user_age(age):
    if age < 6:
        print ("Вы ходите в детский сад")
    elif 7 <=age <17:
        print ("Вы учитесь в школе")
    elif 18 <=age <22:
        print ("Вы учитесь в ВУЗе")
    elif 23<=age <60:
        print ("Вы работаете")
    else:
        print("Неверное значение")

if __name__ == "__main__":
    user_age(your_age)