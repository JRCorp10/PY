def Click():
    res1 = "Bienvenido " + txt.get()
    lbl.configure(text=res1)
    lbl.grid(column=0, row=14)

def Click_2():
    messagebox.showinfo('Hola Mundo','Bienvenidos a JR AO')
    messagebox.showwarning('Hola Mundo', 'Atención!')
    messagebox.showerror('Hola Mundo', 'ERROR FATAL - Tu disco duro ha sido dañado.')
    # OK or yes or retry = TRUE
    # no or cancel = FALSE
    # askyesnocancel = TRUE FALSE y NONE
    res = messagebox.askquestion('Hola Mundo','Desea apagar la computadora?')
    res = messagebox.askyesno('Hola Mundo','Esta seguro?')
    res = messagebox.askyesnocancel('Hola Mundo','Esta seguro de decir que no?')
    res = messagebox.askokcancel('Hola Mundo','Esta seguro de decir que si?')
    res = messagebox.askretrycancel('Hola Mundo','ADIOS')
    messagebox.showinfo('Hola Mundo','MENTIRA IDIOTA.')

def Click_3():
    file = filedialog.askopenfilename()

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
from tkinter import Menu

ventana = Tk()

ventana.geometry('550x450')

ventana.title("Hola Mundo")
lbl = Label(ventana, text="Nombre: ")
lbl = Label(ventana, text="Nombre: ", font=("Arial Bold", 15))
lbl.grid(column=0, row=0)

txt = Entry(ventana,width=10)
txt.focus()
# txt = Entry(ventana,width=10, state='disabled') // Deshabilito opción.
txt.grid(column=1, row=0)

boton = Button(ventana, text="Mostrar")
# boton = Button(ventana, text="Mostrar", bg="orange", fg="red")
boton = Button(ventana, text="Mostrar", command=Click)
boton.grid(column=0, row=2)

combo = Combobox(ventana)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.grid(column=0, row=3)
combo.current(1)

chk_state = BooleanVar()
chk_state.set(False) #set check state
chk = Checkbutton(ventana, text='Confirmar', var=chk_state)
chk.grid(column=0, row=4)

rad1 = Radiobutton(ventana,text='Verdura', value=1)
rad2 = Radiobutton(ventana,text='Carne', value=2)
rad3 = Radiobutton(ventana,text='Fruta', value=3)
rad1.grid(column=1, row=5)
rad2.grid(column=2, row=5)
rad3.grid(column=3, row=5)

rad1 = Radiobutton(ventana,text='Verdura', value=1, command=Click_2)

new_txt = Entry(ventana,width=20)
new_txt.insert(INSERT,'Juani')
new_txt.grid(column=0, row=8)
# new_txt.delete(1,END)

new_btn = Button(ventana,text='Mensaje', command=Click_2)
new_btn.grid(column=0,row=9)


var =IntVar()
var.set(0)
var1 =IntVar()
var1.set(0)
spin = Spinbox(ventana, from_=0, to=10)
spin = Spinbox(ventana, from_=0, to=10, width=5, textvariable=var)
spin.grid(column=0, row=10)
spin = Spinbox(ventana, values=(0, 3, 8, 11), width=5, textvariable=var1)
spin.grid(column=0, row=11)

bar = Progressbar(ventana, length=200)
bar['value'] = 25
bar.grid(column=0, row=12)

boton2 = Button(ventana, text="Abrir Archivo")
boton2 = Button(ventana, text="Abrir Archivo", command=Click_3)
boton2.grid(column=0, row=15)

menu = Menu(ventana)
nombres = Menu(menu)
telefonos = Menu(menu)
dirección = Menu(menu)

nombres.add_command(label='Juani')
nombres.add_separator()
nombres.add_command(label='Santuk')
nombres.add_command(label='Santi')
menu.add_cascade(label='Nombres', menu=nombres)
menu.add_cascade(label='Teléfonos', menu=telefonos)
menu.add_cascade(label='Dirección', menu=dirección)
ventana.config(menu=menu)

ventana.mainloop()

