import random

name = input("Who is asking the question please enter your name: \n")

end_game = "exit"
i = 0
while i != end_game:

    question = input(f"Please enter your question number {i+1} here: \n")

    if question.lower() == end_game:
        print("You have exited the game, Thank you for playing.")
        break

    answer = ""

    random_number = random.randint(1, 9)

    if random_number == 1:
        answer = "Yes - definitely."

    elif random_number == 2:
        answer = "It is decidedly so."

    elif random_number == 3:
        answer = "Without a doubt."

    elif random_number == 4:
        answer = "Reply hazy, try again."

    elif random_number == 5:
        answer = "Ask again later."

    elif random_number == 6:
        answer = "Better not tell you now."

    elif random_number == 7:
        answer = "My sources say no."

    elif random_number == 8:
        answer = "Outlook not so good."

    elif random_number == 9:
        answer = "Very doubtful."

    else:
        answer = "Error."

    print(f"{name} asks:  {question}\n")
    print(f"Magic 8-Ball's answer: {answer}\n")
    print("To exit game type 'EXIT'.")

    i += 1

# print("You have exited the game, Thank you for playing.")