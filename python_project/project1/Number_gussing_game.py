import random
import os

while True:
    ran = random.randint(1, 100)
    count = 1
    print("\n\t-: 🎇 Welcome to the Number Guessing Game 🎇 :-")
    print("     To play the game, guess a number between 1 and 100")

    while True:
        try:
            g = int(input("\n\tYour guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        if g < 1 or g > 100:
            print("⚠️ Your guess is out of range! (1 - 100)")
        elif g == ran:
            print(f"🎉 Congratulations! 🏆 You guessed the number in {count} tries!")
            break
        elif g > ran:
            print("🔻 Too high! Try a smaller number.")
        else:
            print("🔺 Too low! Try a larger number.")

        count += 1

    # Ask if user wants to play again
    choice = input("\n🔁 Do you want to play again?\nPress [Enter] to play again or type 'no' to quit: ").strip().lower()
    if choice == "no":
        print("\n👋 Thanks for playing! Goodbye.")
        break
    else:
        os.system("cls" if os.name == "nt" else "clear")
