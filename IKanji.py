#Imports
import pandas
import random

#Quiz
def quiz(str):
    test=True
    counter=0
    correctCounter=0
    filename='Kanji/'+levelChoice+'.csv'
    df=pandas.read_csv(filename)
    Questions=[random.randint(0, df.shape[0])for iter in range(15)]
    while counter<15:
        meaningAnsw=raw_input("What is the meaning of: "+df["Kanji"][counter]+"? ")
        if meaningAnsw in df["English"][counter]:
            correctCounter+=1
            print("Answer Correct. This kanji means: "+df["English"][counter])
        else:
            print("Answer Incorrect. The answer was: "+df["English"][counter])
        spellingAnsw=raw_input("What is the Onyomi for: "+df["Kanji"][counter]+"? ")
        if spellingAnsw in df["Onyomi"][counter]:
            correctCounter+=1
            print("Answer Correct. This kanji means: "+df["English"][counter])
    print("Quiz ended. Correct Answers "+str(correctCounter)+"/30")    
        counter+=1

#Code Start
print("Learn Kanji N5-N1")
levelChoice=str(raw_input("What would you like to learn? Choices: N5 N4 N3 N2 N1 : "))
print levelChoice
if levelChoice!="N5" and levelChoice!="N4" and levelChoice!="N3" and levelChoice!="N2" and levelChoice!="N1":
    print("Invalid Choice. Please type one of these: N5 N4 N3 N2 N1")
else:
    quiz(levelChoice)
