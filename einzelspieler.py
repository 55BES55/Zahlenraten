import random



def spiel_1():
    n = random.randrange(-100, 100)
    print(f'wenn du aufgibst schreibe "end"')
    z = 10
    while z != 0:
        guess_raw = input("Errate die Zahl: ")
        if guess_raw == "end":
            print("Du hast aufgegeben!")
            break
        try:
            guess = float(guess_raw)
            z = z - 1
            if z == 0:
                print("Du hast keine Versuche mehr")
                print("Du hast verloren")
                break
            elif z != 1:
                print(f"Du hast noch {z} Versuche")
            else:
                print(f"Du hast noch {z} Versuch")

            if guess == n:
                print("Das ist die richtige Zahl!")
                break
            elif guess < n and not z == 0:
                print("Die Zahl ist zu klein! Versuche es nochmal.")
                continue
            elif guess > n and not z == 0:
                print("die Zahl ist zu groß! Versuche es noch mal.")
                continue
        except ValueError:
            print("Schreibe bitte nur Zahlen!")

if __name__ == "__main__":
    spiel_1()