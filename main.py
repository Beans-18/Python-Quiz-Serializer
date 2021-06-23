import pickle

def create_file(quiz):
    handle = open("quiz.pickle", "wb")
    pickle.dump(quiz, handle)

def use_file():
    handle = open("quiz.pickle", "rb")
    return pickle.load(handle)

def play_quiz(quiz):
    points = 0
    for i in quiz:
        if input(i).lower() == quiz[i].lower():
            points = points + 1
            print("Correct!")
        else:
            print("Incorrect.")
    print(f"You got", points, "/", len(quiz), "points in the quiz!")


def create_quiz():
    quiz = {}
    while True:
        if input("Type 'finish' to finish the quiz, or press Enter to create a question: ").lower() == 'finish':
            return quiz
        else:
            first = input("Type what question you would like: ")
            second = input("What would you like the answer to be: ")
            quiz[first] = second

option = input("Would you like to 'create' a quiz or 'play' a quiz you've made?: ").lower()

if option == "create":
    create_file(create_quiz())
elif option == "play":
    play_quiz(use_file())
else:
    print("Invalid input!")
