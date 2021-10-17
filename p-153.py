from tkinter import *
import random

root=Tk()
root.title("Password generator")
root.geometry("500x500")

label1=Label(root)
label2=Label(root)
text_input=Entry(root)
array=[[[0,1,2,3,4,5,6,7,8,9],["Thanos","IRONMAN","THOR","SCORPION"],["A","B","C","D","E","F","G","H","I","J","K","L","M"]]]

def generate():
    label2['text']=str(text_input)
    ran1=random.randint(0,9)
    ran2=random.randint(0,3)
    ran3=random.randint(0,12)
    
    let1=array[0][0][ran1]
    let2=array[0][1][ran2]
    let3=array[0][2][ran3]
    
    label1["text"]=str(let1)+let2+let3
   

button1=Button(root, text="Generate password",command=generate)


text_input.pack()
label2.pack()
button1.pack()
label1.pack()



root.mainloop()