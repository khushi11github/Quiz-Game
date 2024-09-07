# SET OF QUIZ QUESTIONS

import random
n=int(input("Number of total Questions: "))                #No. of total Questions
dict={}                                                    #Questions Directory
score=0
if n>=5:
    for i in range(0,n):
        question=str(input("Question: "))                  #Questions of Quiz
        answer=str(input("Answer: "))                      #Answers of Questions
        if (answer=="True") or (answer=="False"):
            dict.update({question : answer})
        else:
            print("ERROR!!! Enter a valid Answers .i.e., True / False")
    for i in range (0,5):
        print(random.choice(list(dict)))
        ans=str(input(""))
        if (ans =="True") or (ans=="False"):
            if ans==(dict.get(f'{question}')):
                score+=1
    print("score: ",score)
else:
    print("ERROR!!! Enter valid number of Questions to be saved .i.e.,>=5")
