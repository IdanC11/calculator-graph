"""
Author: Idan Chernetsky
Python calculator and graphs of results
"""
# Imports the graphical library
import matplotlib.pyplot as plt

# Welcome message and menu
welcome = '''Welcome to Calculator.py, your options are:
1) Addition
2) Subtraction
3) Multiplication
4) Division
5) Quit calculator
'''
print(welcome)

# Arrays of result
answerList = []
resultList = []
exList = []
countEx = 0


def IsNumber(a):
    """
    Checks if the variable is a number.
    arg: a
    ret: returns type of number (integer/float) or False for string/char
    """
    a = str(a)
    # Negative number indication 
    checkNeg = False
    if a[0] == '-':
        checkNeg = True
    # Checks for a decimal point
    dotCounter = 0

    # Checks for illegal characters
    for i in range(len(a)):
        if dotCounter > 1:
            return False
        if a[i] == '.':
            dotCounter = dotCounter + 1
        elif i != 0 and a[i].isdigit() == False:
            return False

    # Returns a number's type
    if dotCounter == 0:
        return "integer"
    else:
        return "floating"

def FirstNumInput(operation):
    """
    Gets a number
    arg: operation (the operation type and user description)
    ret: A number
    """
    num1 = input(operation + " this: ")
    try:
        print("In try")
        num1 = float(num1)
    except:
        print(":(")
    while type(num1) != float:
        num1 = input("Wrong input, Please insert again: ")
        try:
            print("In try")
            num1 = float(num1)
        except:
            print(":(")
    #while IsNumber(num1) == False:
     #   print("Wrong input, Please insert again: ")
      #  num1 = input(operation, " this: ")
    #if IsNumber(num1) == "integer":
     #   num1 = int(num1)
    #if IsNumber(num1) == "floating":
     #   num1 = float(num1)
    return num1
    

def SecondNumInput(linkWord):
    """
    Gets a number
    arg: linkWord (for the user's convenience)
    ret: A number
    """
    num2 = input(linkWord + " this: ")
    #num2 = str(num2)
    try:
        print("In try")
        num2 = float(num2)
    except:
        print(":(")
    while type(num2) != float:
        num2 = input("Wrong input, Please insert again: ")
        try:
            print("In try")
            num2 = float(num2)
        except:
            print(":(")
#    while IsNumber(num2) == False:
 #       print("Wrong input, Please insert again: ")
  #      num2 = input(linkWord, " this: ")
   # if IsNumber(num2) == "integer":
    #    num2 = int(num2)
    #if IsNumber(num2) == "floating":
    #    num2 = float(num2)
    return num2

def AnswerInput():
    """
    Gets a number and adds it to a list
    arg: 
    ret: A number
    """
    answer = input("Insert your answer: ")
    while IsNumber(answer) == False:
        print("Wrong input, Please insert again: ")
        answer = input("Insert your answer: ")
    if IsNumber(answer) == "integer":
        answer = int(answer)
    else:
        answer = float(answer)
    answerList.append(answer)
    return answer

def Addition():
    """
    Performs Addition between two numbers
    arg: 
    ret: Sum of two numbers + comments
    """
    num1 = FirstNumInput("Add") 
    num2 = SecondNumInput("To")
    answer = AnswerInput()
    result = num1 + num2
    resultList.append(result)
    if answer == result:
        print("Correct!")
    else:
        print("Sorry, the answer should be: ")
        print(num1, " + ", num2, " = ", result)

def Subtraction():
    """
    Performs Subtraction between two numbers
    arg: 
    ret: Subtraction between two numbers + comments
    """
    num1 = FirstNumInput("Subtract")
    num2 = SecondNumInput("From")
    answer = AnswerInput()
    result = num2 - num1
    resultList.append(result)
    if answer == result:
        print("Correct!")
    else:
        print("Sorry, the answer should be: ")
        print(num2, " - ", num1, " = ", result)

def Multiplication():
    """
    Performs Multiplication between two numbers
    arg: 
    ret: Multiplication between two numbers + comments
    """
    num1 = FirstNumInput("Multiply")
    num2 = SecondNumInput("By")
    answer = AnswerInput()
    result = num1 * num2
    resultList.append(result)
    if answer == result:
        print("Correct!")
    else:
        print("Sorry, the answer should be: ")
        print(num1, " X ", num2, " = ", result)

def Division():
    """
    Performs Division between two numbers
    arg: 
    ret: Division between two numbers + comments
    """
    num1 = FirstNumInput("Divide")
    num2 = SecondNumInput("By")
    answer = AnswerInput()
    result = num1 / num2
    resultList.append(result)
    if answer == result:
        print("Correct!")
    else:
        print("Sorry, the answer should be: ")
        print(num1, " : ", num2, " = ", result)

# User's options 
choose = 1
while choose != 5:
    choose = input("Choose your option: ")
    try:
        print("In try")
        choose = int(choose)
        #print(type(int(choose)))
    except:
        print(":(")
        
    while type(choose) != int:
        choose = input("Wrong input, Please insert again: ")
        try:
            choose = int(choose)
        except:
            print(":(")
       
    if choose == 1:
        countEx = countEx + 1
        exList.append(countEx)
        Addition()
    if choose == 2:
        countEx = countEx + 1
        exList.append(countEx)
        Subtraction()
    if choose == 3:
        countEx = countEx + 1
        exList.append(countEx)
        Multiplication()
    if choose == 4:
        countEx = countEx + 1
        exList.append(countEx)
        Division()

# Prints a graph of the answers and result by the exercise's index
plt.plot(exList, resultList, label = 'True Results')
plt.plot(exList, answerList, label = 'Answers')
plt.xlabel('Exercise Index')
plt.ylabel('Result/Answers')
plt.title('Calculator')
plt.show()
