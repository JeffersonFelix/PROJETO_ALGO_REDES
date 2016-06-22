from tkinter import messagebox
from FUNÇÕES3 import funcao_nmap
from tkinter import *

root = Tk()

root.title('Link Teste')
root.configure(background='#696969')
#LxA+E+T
#600x450+370+200
root.geometry('600x450+370+200')

lab_1 = Label(root,text='Informe o Alvo:',bg='#696969', font=('arial', 12))
lab_2 = Label(root,text='',bg='#696969')
lab_3 = Label(root,text= 'TESTANDO A CONEXÃO', fg='#000000',bg='#696969', font=('arial black', 18))
ent_1 = Entry(root,width='16') #width: regula a resolução
Cap1 = PhotoImage(file='Cap1.GIF',)
rot_1= Label(root, image=Cap1,bg='#696969')

def printName():

    funcao_nmap(ent_1.get())
    relatorio = open('relatorio.txt', 'a')
    #relatorio.write('Host: ')
    relatorio.write(ent_1.get())
    relatorio.close()
    messagebox.showinfo("O relatório ", "Seu Relatório foi salvo com êxito.")
    print(ent_1.get())

but_2 = Button(root, width='13', text='Gerar', bg='#696969', command=printName)
but_2.place(x=250, y=340)

lab_1.place(x=248, y=298)
lab_2.place(x=350, y=280)
lab_3.place(x=145, y=260)
ent_1.place(x=250, y=320)
rot_1.place(x=175, y=1)

root.mainloop()


















