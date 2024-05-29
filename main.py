score=0
play= "yes"

#Ask the user their name
name= input("What's your name?")

#Greet the user and introduce the quiz
print("Welcome to this quiz")
print("This quiz is about capital cities of the world")

# Check number of question attempts
while True:
    try:
        tries = input("How many attempts do you want at each question? 1-4")
        tries = int(tries)
        break
    except:
        print("That's not number")

# Start the quiz
while play =="yes":

    question_attempts=tries
    while question_attempts > 0:
        # Ask the user a question
        question ="What is the capital of New Zealand?"
        a ="Wellington"
        b ="Auckland"
        c ="London"
        d ="Christchurch"
        answer = input("{}\nA.{} B.{}C.{}D.{}".format(question, a, b, c, d)).lower()

        # Check the user's answer
        if answer == a or answer =="a":
            print("Corect")
            score +=5
            break
        elif answer == "":
            print("Not sure?")
        elif answer != a and answer !="a" and answer !="b" and answer != c and answer != d and answer !="d":
            print("That wasn't an option")
        else:
            print("Wrong!")

        question_attempts -= 1
    print("The answer os Wellington.")

    #End the quiz
    print("Well done {}. You finished the quiz. Your final score was {}".format(name,score))

    # Replay
    play = input("Do you want to play again?").lower()


