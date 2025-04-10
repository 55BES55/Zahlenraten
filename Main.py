import einzelspieler
import zweispieler

while True:
    player = input("Willst du ein oder zweispieler spielen? (1/2)")
    if player == "1":
        einzelspieler.spiel_1()
    elif player == "2":
        zweispieler.spiel_2()


    jn = input("\nWillst du Nochmal spielen? (j/n): ").strip().lower()
    if not jn.startswith("j"):
        print("Auf Wiedersehen! 👋")
        break
