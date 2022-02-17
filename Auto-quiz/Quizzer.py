import random


inp = input("Enter SRC : ")


alpha = open("Datafiles\\" + inp + ".txt" ,'r')
xta = alpha.read()
xta2 = xta.split("\n")
questions = []
answers = []


for i in range(len(xta2)):
    if("Question" in xta2[i]):
        questions.append(xta2[i])
    if("Answer" in xta2[i]):
        answers.append(xta2[i])
        

indices = []

for i in range(len(questions)-1):
    indices.append(i-1)


random.shuffle(indices)

for i in range(len(indices)):
    print(questions[indices[i]])
    x = input("")
    print("")
    print(answers[indices[i]])
    a = input("")
    print("==============================================================================================================================================================")
    
