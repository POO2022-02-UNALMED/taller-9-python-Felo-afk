from tkinter import Tk, Button, Entry, END

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0, 0)
root.geometry("310x265")

# Configuración pantalla de salida
pantalla = Entry(root, width=40, bg="black", fg="white",
                 borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=40, padx=1, pady=1)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red",
                 borderwidth=0, cursor="hand2", command=lambda: getShow('1')).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red",
                 borderwidth=0, cursor="hand2", command=lambda: getShow('2')).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red",
                 borderwidth=0, cursor="hand2", command=lambda: getShow('3')).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red",
                 borderwidth=0, cursor="hand2", command=lambda: getShow('4')).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red",
                 borderwidth=0, cursor="hand2", command=lambda: getShow('5')).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red",
                 borderwidth=0, cursor="hand2", command=lambda: getShow('6')).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red",
                 borderwidth=0, cursor="hand2", command=lambda: getShow('7')).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red",
                 borderwidth=0, cursor="hand2", command=lambda: getShow('8')).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red",
                 borderwidth=0, cursor="hand2", command=lambda: getShow('9')).grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white",
                     borderwidth=0, cursor=" hand2", command=lambda: igual()).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green",
                     fg="black", cursor="hand2", borderwidth=0, command=lambda: getShow(".")).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black",
                   borderwidth=0, cursor="hand2", command=lambda: sumar()).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue",
                     fg="black", borderwidth=0, cursor="hand2", command=lambda: restar()).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue",
                              fg="black", borderwidth=0, cursor="hand2", command=lambda: multiplicar()).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue",
                        fg="black", borderwidth=0, cursor="hand2", command=lambda: dividir()).grid(row=4, column=3, padx=1, pady=1)
# Eventos


def operar(op):

    if op == 1:
        pantalla.insert(0, operador + operando)
    if op == 2:
        pantalla.insert(0, operador - operando)
    if op == 3:
        pantalla.insert(0, operador * operando)
    if op == 4:
        pantalla.insert(0, operador / operando)


def getShow(v):
    b = pantalla.get()
    pantalla.delete(0, END)
    t = str(b+v)
    pantalla.insert(0, t)


def igual():
    global operando
    operando = float(pantalla.get())
    pantalla.delete(0, END)
    operar(operacion)


def sumar():
    global operacion
    global operador
    operador = float(pantalla.get())
    operacion = 1
    pantalla.delete(0, END)


def restar():
    global operacion
    global operador
    operador = float(pantalla.get())
    operacion = 2
    pantalla.delete(0, END)


def multiplicar():
    global operacion
    global operador
    operador = float(pantalla.get())
    operacion = 3
    pantalla.delete(0, END)


def dividir():
    global operacion
    global operador
    operador = float(pantalla.get())
    operacion = 4
    pantalla.delete(0, END)


root.mainloop()
