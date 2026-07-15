from src.calpakg.calculator import add, subtract
from src.game.Galaxy import Game

def run_calculator():
    print("Haloo")
    print(add(5, 3))
    print(subtract(5, 3))

def run_game():
    Game().run()

if __name__ == "__main__":
    print("เลือกโปรแกรมที่จะรัน:")
    print("1. Calculator")
    print("2. Game")
    choice = input("กรอกเลข (1/2): ")

    if choice == "1":
        run_calculator()
    elif choice == "2":
        run_game()
    else:
        print("เลือกไม่ถูกต้อง")
