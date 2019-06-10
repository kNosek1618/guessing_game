
secret_word = "loudness"
guess = ""
i = 1

while guess != secret_word:
    guess = input("Enter guess: ")
    if i <= 2:
        i += 1
        print("try again,")
    elif i == 2:
        break




print("You've learned the secret!")