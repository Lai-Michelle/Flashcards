#from graphics import *

def createSet():
    "prompts user to enter term and definition"
    setTitle = str(input("What is the title of this set? "))

    questions = []
    answers = []
    #while user hasn't said create:
    inputQuestion = str(input("Term "))
    inputAnswer = str(input("Definition "))

    questions.append(inputQuestion)
    answers.append(inputAnswer)

    myfile = open("[].txt", "w")
    for i in range(len(questions)):
        terms = questions[i] + ";" + answers[i]
        myfile.write(terms + "\n")

    myfile.close()

    return ([setTitle, myfile])

def displayHome():
    "creates the image of flashcard with term and definition"
    print("in displayHome()")
    #display Quizlet button, search bar, account icon at top
    #list recent study sets with title and username ("guest" if no account)

def studySet():
    "creates display of flashcard and different study options"
    term = []

    myfile = open("flashcardfile.txt", "r")
    for line in myfile:
        lineList = line.split(";")
        question = lineList[0]
        answer = lineList[1]
        term.append([question, answer])
    myfile.close()
    return term

def main():
    print("Welcome to Quizlet!")

    displayHome()

    create = str(input("Would you like to create a new set? "))
    if create == "Yes" or create == "yes": #chooses to create a new set
        newSet = createSet()
        print(newSet)
    elif create == "No" or create == "no":
        study = str(input("Would you like to study your set? "))
        if study == "Yes" or "yes": #chooses to study a set
            useSet = studySet()
            print(useSet[0:15])

main()
