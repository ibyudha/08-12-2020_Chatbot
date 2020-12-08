"""
Created on Tue Dec  8 14:33:06 2020

@author: Gus Yudha
"""

from tkinter import *
app=Tk()
def submit():
    submit="Anda:"+a.get()
    printChatnya.insert(END,"\n"+submit)
    if(a.get()=='hai'):
        printChatnya.insert(END,"\n" + "Bot:halo")
    elif(a.get()=='halo'):
        printChatnya.insert(END,"\n"+ "Bot:hai")
    elif(a.get()=='Kamu siapa?'):
        printChatnya.insert(END,"\n"+ "Bot:Aku Bot, kamu?")
    elif(a.get()=='saya gus yudha'):
        printChatnya.insert(END,"\n"+ "Bot:Ntapss, halo gus yudha")
    else:
        printChatnya.insert(END,"\n"+ "Bot:Maaf, saya tidak mengerti :( ")
printChatnya=Text(app,bg='white')
printChatnya.grid(row=0,column=0,columnspan=2)
a=Entry(app,width=80)
submit=Button(app,text='Kirim',bg='white',width=20,command=submit).grid(row=1,column=1)
a.grid(row=1,column=0)
app.title('Chatbot Sederhana')
app.mainloop()