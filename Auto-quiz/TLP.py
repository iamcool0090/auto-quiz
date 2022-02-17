import time
import os
import pyautogui
from tkinter import *
import docx
from nltk import tokenize
import pandas as pd
import random
import re



global doc
doc = docx.Document()

ques = ""
answ = ""

global is_image

is_image = False


chap = input("Please Enter the chapter name : ")

#reading and indentifying chemmical compounds and formulas
a = pd.read_excel(r"Database\a.xlsx")
df = pd.DataFrame(a)

names = []
formulas = []

for i in range(len(df["LOWNAME"])):
	names.append([df['LOWNAME'][i]])
	formulas.append(df['Chemical formula'][i])

temp_a = []	
def find(a):
    return a in formulas

def find_name(a):
        temp_a.append(a.lower())

        if(temp_a in names):
                temp_a.clear()
                return True
        else:
                temp_a.clear()
                return False


#deletetion of unwanted words 

unwanted_words = pd.read_excel(r"Database\common_words.xlsx")

df2 = pd.DataFrame(unwanted_words)
word_avoidlist = []

for i in range(len(df2["Words"])):
        word_avoidlist.append(df2['Words'][i])


processes = pd.read_excel(r"Database\processes.xlsx")
dfrex = pd.DataFrame(processes)
rex = []
for i in range(len(dfrex['process'])):
        rex.append(dfrex['process'][i])


character = pd.read_excel(r"Database\character.xlsx")
dfcha = pd.DataFrame(character)

cha = []
for i in range(len(dfcha['character'])):
        cha.append(dfcha['character'][i])

reag = pd.read_excel(r"Database\reagents.xlsx")
dfrea = pd.DataFrame(reag)

rea = []
rea2 = []
for i in range(len(dfrea['Name'])):
        rea.append(dfrea['Name'][i])
        rea2.append(dfrea['name'][i])
        
organic = pd.read_excel(r"Database\organic.xlsx")
dfor = pd.DataFrame(organic)

organic_compounds = []
organic_compounds2 = []

for i in range(len(dfor['org'])):
        organic_compounds.append(dfor['org'][i])
        organic_compounds2.append(dfor['Org'][i])

organic_compounds2[248] = "sad"
orx2a = []
orxa = []

for i in range(len(organic_compounds2)):
        orx2a.append(organic_compounds2[i].replace("\xa0",""))

for i in range(len(organic_compounds)):
        orxa.append(organic_compounds[i].replace("\xa0",""))


        
#primary filter
def gen():
        ge = ""
        ques = question.get("1.0",'end-1c')
        question.delete("1.0","end")
        ges = ques.split(".")
        
        for i in range(len(ges)):
                ge = ge + ges[i] + "."

        ge = ge.replace("\n"," ")
        fy = ge
        
        zy = fy
        zy = zy.replace("sulphur","sulfur")
        ty = fy
        ty = ty.replace("sulphur","sulfur")
        ty = ty.replace("'","")
        ty = ty.replace("’",'')
        ty = ty.replace("–",'')
        ty = ty.replace("(",' ')
        ty = ty.replace(")",'')



        st = ty.split()
        st[len(st)-1] = st[len(st)-1].replace(".","")
        st2 = []


        for i in range(len(st)):
                                          
                if st[i] in word_avoidlist:
                        st2.append(st[i])



        f1 = list(set(st) - set(st2))



                #secondary filter


        f1mask = []
        for i in range(len(f1)):
                tempa = f1[i].replace(",","")
                tem2 = tempa
                tem = tempa.lower()
                temp_lis = []
                temp_lis.append(tem)
                        
                        
                if temp_lis in names or tem2 in formulas or tem2 in rex or tem2 in cha or tem2 in orxa or tem2 in orx2a or tem2 in rea or tem2 in rea2:
                        f1mask.append(f1[i])
                        temp_lis.clear()
                else:
                        temp_lis.clear()
                        pass

                        
        for i in range(len(f1mask)):
                f1mask[i] = re.sub(',','', f1mask[i])


        f2 = list(set(f1)-set(f1mask))



        ques = ""
        jh = [] 
        for i in range(len(f1mask)):
                jh.append(zy.replace(f1mask[i],len(f1mask[i]) * "_"))

        src = "Datafiles\\" + chap + ".txt"
        
        for i in range(len(jh)):
                qp = ""
                ansq = ""
                
                qp = "Question : " + jh[i]
                ansq = "Answer : " + f1mask[i]
                
                
                print(qp,file=open(src,"a"))
                print(ansq,file=open(src,"a"))
                print(" ", file=open(src,"a"))               
                

                

                
  



        
root = Tk()


root.title("Auto-Quiz!!")
root.configure(bg='#0080ff')
root.geometry('700x500')



question = Text(root, height = 10, width = 85, bg = "light yellow")
question.pack()





com = Button(root, text = 'SUBMIT!!', width = 10, height = 1,command = gen)
com.pack()


root.mainloop()


