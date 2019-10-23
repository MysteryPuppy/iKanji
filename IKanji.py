#!/usr/bin/python

#Imports
import pandas
import random

#Quiz
def quiz(x):
    test=True
    counter=0
    correctCounter=0
    filename='Kanji/'+levelChoice+'.csv'
    df=pandas.read_csv(filename)
    Questions=[random.randint(0, df.shape[0])for iter in range(10)]
    print("Quiz Started - "+levelChoice)
    optionsChoice=raw_input("Would you like to do 1. Meanings or 2. Meanings + Onyomi + Kunyomi? \n>")
    while counter<10:
        #Meaning
        print("Question "+str(counter)+".")
        meaningAnsw=raw_input("What is the meaning of: "+df["Kanji"][Questions[counter]]+"? \n>")
        if meaningAnsw in df["English"][Questions[counter]]:
            correctCounter+=1
            print("Answer Correct. This kanji means: "+df["English"][Questions[counter]])
        else:
            print("Answer Incorrect. The answer was: "+df["English"][Questions[counter]])
        if optionsChoice=="2":
            #Onyomi
            onyomiAnsw=raw_input("What is the Onyomi for: "+df["Kanji"][Questions[counter]]+"? \n>")
            if onyomiAnsw in df["Onyomi"][Questions[counter]]:
                correctCounter+=1
                print("Answer Correct. This kanji's Onyomi is: "+df["Onyomi"][Questions[counter]])
            else:
                print("Answer Incorrect. The answer was: "+df["Onyomi"][Questions[counter]])
            #Kunyomi
            onyomiAnsw=raw_input("What is the Kunyomi for: "+df["Kanji"][Questions[counter]]+"? \n>")
            if onyomiAnsw in df["Kunyomi"][Questions[counter]]:
                correctCounter+=1
                print("Answer Correct. This kanji's Kunyomi is: "+df["Kunyomi"][Questions[counter]])
            else:
                print("Answer Incorrect. The answer was: "+df["Kunyomi"][Questions[counter]])
        counter+=1
    #End of quiz
    if optionsChoice=="2":
        print("Quiz ended. Correct Answers "+ str(correctCounter) +"/30")
    else:
        print("Quiz ended. Correct Answers "+ str(correctCounter) +"/10")

#Code Start
starter=True
while starter==True:
    print("Learn Kanji N5-N1")
    levelChoice=(str(raw_input("What would you like to learn? Choices: N5 N4 N3 N2 N1 or Quit: \n>"))).upper()
    if levelChoice!="N5" and levelChoice!="N4" and levelChoice!="N3" and levelChoice!="N2" and levelChoice!="N1" and levelChoice!="QUIT":
        print("Invalid Choice. Please type one of these: N5 N4 N3 N2 N1")
    elif levelChoice=="QUIT":
        starter==False
        break
    elif levelChoice=="N2" or levelChoice=="N1":
        print("CSV files for these kanji have not been found as of yet.")
    else:
        quiz(levelChoice)
