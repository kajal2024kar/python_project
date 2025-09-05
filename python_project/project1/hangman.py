import random
import time

hints = ["Scary, floats", "Sand and water", "Shows happiness", "Makes things red, blue, etc.", "Stays on top of water", "Challenging to put together", "Lets you see outside",  "Speak very softly", "Captures pictures", "Colorful arc after rain", "What you learn and know",  "Beautiful flying insect", "Very grand or impressive", "Place you go to eat", "Makes lights work", "What you say to someone who wins", "A chance to do something", "Unusual event", "The words you know", "Being accountable for something",
]

words = ["Ghost", "Beach", "Smile", "Color", "Float", "Puzzle", "Window", "Whisper", "Camera", "Rainbow", "Knowledge", "Butterfly", "Magnificent", "Restaurant", "Electricity", "Congratulations", "Opportunity", "Phenomenon", "Vocabulary", "Responsibility"
]

def dash(word):
    global ol
    for i in range(len(word)):
        print(ol[i], end=" ")
        time.sleep(0.2)
    print()

def game_on():
    ask=input("do you want to play again .enter yes or no.").lower()
    if ask=="yes":
        return 'yes'
    elif ask=="no":
        return "break"
    else:
        print("invalid text.")
        return "break"
print("----------WELCOME TO THE GAME OF HANGMAN---------- .\n")
name=input("Enter your name.\n")
print(f"Lets begin {name}!!!\n")
idx=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
while True:
    a=random.choice(idx)
    idx.remove(a)
    print(f"HINT: {hints[a]} \n")
    word=words[a].upper()
    ol=["_" for i in range(len(word))]
    dash(word)
    attempt=5
    guessed=[]
    if "_" not in ol: print(f"you won !! you guessed the word correctly. \nyour score is: {attempt*10} \n")
    while attempt> 0:
        if "_" in ol:
            ans=input("Enter an alphabet or word : \n").upper()
            if ans in guessed:
                print("you have already guessed the alphabet ! \n")
                continue
            elif ans==word:
                print(f"you guessed the word correctly. \nYour Score is : {attempt*10}\n")
                break
            else:
                guessed.append(ans)
                if ans not in word:
                    attempt=attempt-1
                    print(f"its wrong !. you have {attempt} chances left \n")

                if ans in word:
                    attempt=attempt-1
                    for i in range(len(word)):
                        if word[i]==ans:
                            ol[i]=ans
                    print(f"it's correct ! you have {attempt} chances left. \n ")

                dash(word)
    else:
        print("you lost")
        print(f"the word was: {word} \nYour score is 0. ")
    g=game_on()
    if g=="break":
        break