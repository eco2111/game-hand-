import random

def user_choice():
    print("Tanlovingizni kiriting: ")
    print("1 - Tosh")
    print("2 - Qaychi")
    print("3 - Qog'oz")
    choice = input("Tanlovni kiriting (1/2/3): ")
    if choice == "1":
        return "Tosh"
    elif choice == "2":
        return "Qaychi"
    elif choice == "3":
        return "Qog'oz"
    else:
        print("Noto'g'ri tanlov! Iltimos, yana bir bor urinib ko'ring.")
        return user_choice()

def computer_choice():
    return random.choice(["Tosh", "Qaychi", "Qog'oz"])

def determine_winner(user, computer):
    if user == computer:
        return "Durrang! Ikki tomon ham bir xil tanlovni qildi."
    elif (user == "Tosh" and computer == "Qaychi") or \
         (user == "Qaychi" and computer == "Qog'oz") or \
         (user == "Qog'oz" and computer == "Tosh"):
        return "Siz yutdingiz!"
    else:
        return "Kompyuter yutdi!"

def play_game():
    user = user_choice()
    computer = computer_choice()
    print(f"Kompyuter tanlovi: {computer}")
    result = determine_winner(user, computer)
    print(result)

if __name__ == "__main__":
    play_game()