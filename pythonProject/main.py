import numpy as np
from tkinter import *
from sympy import *
from tkinter import ttk
from sympy import var
from PIL import ImageTk, Image

ws = Tk()
ws.title('Numerical Analysis')
ws.geometry('700x450')
ws.config(bg='yellow')
img = ImageTk.PhotoImage(file="bgpicc.png")
label = Label(ws, image=img )
label.place(x=0, y=0)

# Create a Canvas
canvas = Canvas(ws, width=700, height=3500)
canvas.pack(fill=BOTH, expand=True)

# Add Image inside the Canvas
canvas.create_image(0, 0, image=img, anchor='nw')


# Function to resize the window
def resize_image(e):
    global image, resized, image2
    # open image to resize it
    image = Image.open("bgpicc.png")
    # resize the image with width and height of root
    resized = image.resize((e.width, e.height), Image.ANTIALIAS )
    image2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=image2, anchor='nw')
# Bind the function to configure the parent window
ws.bind("<Configure>", resize_image)

def secant():
    # create window
    secant_window = Tk()
    secant_window.title('Secant Method')
    canvas1 = Canvas(secant_window, width=800, height=400, relief='raised')
    canvas1.pack()

    # equation
    label1 = Label(secant_window, text='Enter function ( f(x) ) : ')
    label1.config(font=('sans-serif', 10))
    canvas1.create_window(300, 80, window=label1)
    entry1 = Entry(secant_window)
    canvas1.create_window(430, 80, window=entry1)

    # Xu
    label2 = Label(secant_window, text='Xi-1:')
    label2.config(font=('sans-serif', 10))
    canvas1.create_window(140, 150, window=label2)
    entry2 = Entry(secant_window)
    canvas1.create_window(220, 150, window=entry2)

    # Xl
    label3 = Label(secant_window, text='Xi:')
    label3.config(font=('sans-serif', 10))
    canvas1.create_window(340, 150, window=label3)
    entry3 = Entry(secant_window)
    canvas1.create_window(420, 150, window=entry3)

    # Error
    label4 = Label(secant_window, text='Error:')
    label4.config(font=('sans-serif', 10))
    canvas1.create_window(540, 150, window=label4)
    entry4 = Entry(secant_window)
    canvas1.create_window(620, 150, window=entry4)

    def solve_method():
        x1 = entry1.get()
        global x
        x = var('x')  # the possible variable names must be known beforehand...
        global f
        f = sympify(x1)
        ximin1 = float(entry2.get())
        xi = float(entry3.get())
        global eps
        eps = float(entry4.get())
        secant_method(ximin1, xi)

    button1 = Button(secant_window, text='solve', command=solve_method, bg='#2873D8', fg='white',
                     font=('helvetica', 9, 'bold'))
    canvas1.create_window(400, 230, window=button1)

    # table
    my_table = ttk.Treeview(secant_window)
    my_table['columns'] = ('i', 'xi-1', 'f(xi-1)', 'xi', 'f(xi)', 'Error')

    my_table.column("#0", width=0, stretch=NO)
    my_table.column("i", anchor=CENTER, width=80)
    my_table.column("xi-1", anchor=CENTER, width=100)
    my_table.column("f(xi-1)", anchor=CENTER, width=120)
    my_table.column("xi", anchor=CENTER, width=100)
    my_table.column("f(xi)", anchor=CENTER, width=120)
    my_table.column("Error", anchor=CENTER, width=120)

    my_table.heading("#0", text="", anchor=CENTER)
    my_table.heading("i", text="I", anchor=CENTER)
    my_table.heading("xi-1", text="Xi-1", anchor=CENTER)
    my_table.heading("f(xi-1)", text="f(xi-1)", anchor=CENTER)
    my_table.heading("xi", text="xi", anchor=CENTER)
    my_table.heading("f(xi)", text="f(xi)", anchor=CENTER)
    my_table.heading("Error", text="Error", anchor=CENTER)
    canvas1.create_window(410, 400, window=my_table)

    def secant_method(ximin1, xi):

        step = 0
        condition=True
        while condition:
            xiPlus1 = xi - (f.subs(x, xi)* (ximin1 - xi)) / (f.subs(x, ximin1)- f.subs(x, xi))
            if step == 0:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, ximin1, f.subs(x, ximin1), xi, f.subs(x, xi), "-"))
                error = abs((xiPlus1 - xi) / xiPlus1) * 100
            else:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, ximin1, f.subs(x, ximin1), xi, f.subs(x, xi), error))
            step = step + 1
            condition=error>eps
            error = abs((xiPlus1 - xi) / xiPlus1) * 100
            if error<eps:
                # print the root
                rootlabel = Label(secant_window, text="Root=")  # shows as text in the window
                rootlabel.config(font=('sans-serif', 10))
                canvas1.create_window(540, 230, window=rootlabel)
                root = Label(secant_window, text=xi)
                root.config(font=('sans-serif', 10))
                canvas1.create_window(620, 230, window=root)
            ximin1 = xi;
            xi = xiPlus1

    secant_window.mainloop()
def simple():
    # create window
    FixedPoint_window = Tk()
    FixedPoint_window.title('Simple fixed point Method')
    canvas1 = Canvas(FixedPoint_window, width=800, height=400, relief='raised')
    canvas1.pack()

    # equation f(x)
    label1 = Label(FixedPoint_window, text='Enter function ( f(x) ) : ')
    label1.config(font=('sans-serif', 10))
    canvas1.create_window(130, 80, window=label1)
    entry1 = Entry(FixedPoint_window)
    canvas1.create_window(270, 80, window=entry1)

    # equation g(x)
    label2 = Label(FixedPoint_window, text='Enter function ( g(x) ) : ')
    label2.config(font=('sans-serif', 10))
    canvas1.create_window(450, 80, window=label2)
    entry2 = Entry(FixedPoint_window)
    canvas1.create_window(600, 80, window=entry2)

    # Xi
    label3 = Label(FixedPoint_window, text='Xi:')
    label3.config(font=('sans-serif', 10))
    canvas1.create_window(130, 150, window=label3)
    entry3 = Entry(FixedPoint_window)
    canvas1.create_window(270, 150, window=entry3)

    # Error
    label4 = Label(FixedPoint_window, text='Error:')
    label4.config(font=('sans-serif', 10))
    canvas1.create_window(450, 150, window=label4)
    entry4 = Entry(FixedPoint_window)
    canvas1.create_window(600, 150, window=entry4)

    def solve_method():
        x1 = entry1.get()
        x2 = entry2.get()
        global x
        x = var('x')  # the possible variable names must be known beforehand...
        global f
        global g
        f = sympify(x1)
        g = sympify(x2)
        xi = float(entry3.get())
        global eps
        eps = float(entry4.get())
        fixedpoint_method(xi)

    button1 = Button(FixedPoint_window, text='solve', command=solve_method, bg='#2873D8', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(400, 230, window=button1)

    # table
    my_table = ttk.Treeview(FixedPoint_window)
    my_table['columns'] = ('i', 'xi', 'f(xi)', 'Error')

    my_table.column("#0", width=0, stretch=NO)
    my_table.column("i", anchor=CENTER, width=80)
    my_table.column("xi", anchor=CENTER, width=100)
    my_table.column("f(xi)", anchor=CENTER, width=120)
    my_table.column("Error", anchor=CENTER, width=120)

    my_table.heading("#0", text="", anchor=CENTER)
    my_table.heading("i", text="I", anchor=CENTER)
    my_table.heading("xi", text="Xi", anchor=CENTER)
    my_table.heading("f(xi)", text="f(xi)", anchor=CENTER)
    my_table.heading("Error", text="Error", anchor=CENTER)
    canvas1.create_window(410, 400, window=my_table)

    def fixedpoint_method(xi):
        step = 0
        condtion = True
        while condtion:
            xiplus1 = g.subs(x, xi)
            if step == 0:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, xi, xiplus1, "-"))
                error = abs((xiplus1 - xi) / xiplus1) * 100
            else:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, xi, xiplus1, error))
            step = step + 1
            condtion = error > eps
            error = abs((xiplus1 - xi) / xiplus1) * 100
            if error<eps:
                rootlabel = Label(FixedPoint_window, text="Root=")  # shows as text in the window
                rootlabel.config(font=('sans-serif', 10))
                canvas1.create_window(540, 230, window=rootlabel)
                root = Label(FixedPoint_window, text=xi)  # shows as text in the window
                root.config(font=('sans-serif', 10))
                canvas1.create_window(620, 230, window=root)
            xi = xiplus1

    FixedPoint_window.mainloop()
def bisection():

    # create window
    bisec_window = Tk()
    bisec_window.title('Bisection Method')
    canvas1 = Canvas(bisec_window, width=800, height=400, relief='raised')
    canvas1.pack()

    # equation
    label1 = Label(bisec_window, text='Enter function ( f(x) ) : ')
    label1.config(font=('sans-serif', 10))
    canvas1.create_window(300, 80, window=label1)
    entry1 = Entry(bisec_window)
    canvas1.create_window(430, 80, window=entry1)

    # Xu
    label2 = Label(bisec_window, text='Xu:')
    label2.config(font=('sans-serif', 10))
    canvas1.create_window(140, 150, window=label2)
    entry2 = Entry(bisec_window)
    canvas1.create_window(220, 150, window=entry2)

    # Xl
    label3 = Label(bisec_window, text='Xl:')
    label3.config(font=('sans-serif', 10))
    canvas1.create_window(340, 150, window=label3)
    entry3 = Entry(bisec_window)
    canvas1.create_window(420, 150, window=entry3)

    # Error
    label4 = Label(bisec_window, text='Error:')
    label4.config(font=('sans-serif', 10))
    canvas1.create_window(540, 150, window=label4)
    entry4 = Entry(bisec_window)
    canvas1.create_window(620, 150, window=entry4)

    def solve_method():
        x1 = entry1.get()
        global x
        x = var('x')  # the possible variable names must be known beforehand...
        global f
        f = sympify(x1)
        xu = float(entry2.get())
        xl = float(entry3.get())
        global eps
        eps = float(entry4.get())
        bisection_method(xl, xu)

    button1 = Button(bisec_window ,text='solve', command=solve_method, bg='#2873D8', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(400, 230, window=button1)

    # table
    my_table = ttk.Treeview(bisec_window)
    my_table['columns'] = ('i', 'xl', 'f(xl)', 'xu', 'f(xu)', 'xr', 'f(xr)', 'Error')

    my_table.column("#0", width=0, stretch=NO)
    my_table.column("i", anchor=CENTER, width=80)
    my_table.column("xl", anchor=CENTER, width=100)
    my_table.column("f(xl)", anchor=CENTER, width=120)
    my_table.column("xu", anchor=CENTER, width=100)
    my_table.column("f(xu)", anchor=CENTER, width=120)
    my_table.column("xr", anchor=CENTER, width=100)
    my_table.column("f(xr)", anchor=CENTER, width=120)
    my_table.column("Error", anchor=CENTER, width=120)

    my_table.heading("#0", text="", anchor=CENTER)
    my_table.heading("i", text="I", anchor=CENTER)
    my_table.heading("xl", text="Xl", anchor=CENTER)
    my_table.heading("f(xl)", text="f(xl)", anchor=CENTER)
    my_table.heading("xu", text="Xu", anchor=CENTER)
    my_table.heading("f(xu)", text="f(xu)", anchor=CENTER)
    my_table.heading("xr", text="Xr", anchor=CENTER)
    my_table.heading("f(xr)", text="f(xr)", anchor=CENTER)
    my_table.heading("Error", text="Error", anchor=CENTER)
    canvas1.create_window(410, 400, window=my_table)

    def bisection_method(xl, xu):
        error = abs(xu - xl) * 100
        xr = 0
        step = 0
        if f.subs(x, xl) * f.subs(x, xu) >= 0:
            lable5 = Label(bisec_window, text='no root or multiple roots present')
            canvas1.create_window(400, 400, window=lable5)
            quit()
        while error > eps:
            xrold = xr
            xr = (xu + xl) / 2
            error = abs((xr - xrold) / xr) * 100
            if step == 0:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, xl, f.subs(x, xl), xu, f.subs(x, xu), xr, f.subs(x, xr), "-"))
            else:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, xl, f.subs(x, xl), xu, f.subs(x, xu), xr, f.subs(x, xr), error))
            step = step + 1
            if f.subs(x, xr) * f.subs(x, xl) < 0:
                xu = xr
            elif f.subs(x, xr) * f.subs(x, xu) < 0:
                xl = xr
            else:
                quit()
        printroot(xr)

    def printroot(xr):

        rootlabel = Label(bisec_window, text="Root=")  # shows as text in the window
        rootlabel.config(font=('sans-serif', 10))
        canvas1.create_window(540, 230, window=rootlabel)
        root = Label(bisec_window, text=xr)  # shows as text in the window
        root.config(font=('sans-serif', 10))
        canvas1.create_window(620, 230, window=root)
    bisec_window.mainloop()
def falsepos():

    # create window
    FalsePosition_window = Tk()
    FalsePosition_window.title('False Position Method')
    canvas1 = Canvas(FalsePosition_window, width=800, height=400, relief='raised')
    canvas1.pack()

    # equation
    label1 = Label(FalsePosition_window, text='Enter function ( f(x) ) : ')
    label1.config(font=('sans-serif', 10))
    canvas1.create_window(300, 80, window=label1)
    entry1 = Entry(FalsePosition_window)
    canvas1.create_window(430, 80, window=entry1)

    # Xu
    label2 = Label(FalsePosition_window, text='Xu:')
    label2.config(font=('sans-serif', 10))
    canvas1.create_window(140, 150, window=label2)
    entry2 = Entry(FalsePosition_window)
    canvas1.create_window(220, 150, window=entry2)

    # Xl
    label3 = Label(FalsePosition_window, text='Xl:')
    label3.config(font=('sans-serif', 10))
    canvas1.create_window(340, 150, window=label3)
    entry3 = Entry(FalsePosition_window)
    canvas1.create_window(420, 150, window=entry3)

    # Error
    label4 = Label(FalsePosition_window, text='Error:')
    label4.config(font=('sans-serif', 10))
    canvas1.create_window(540, 150, window=label4)
    entry4 = Entry(FalsePosition_window)
    canvas1.create_window(620, 150, window=entry4)

    def solve_method():
        x1 = entry1.get()
        global x
        x = var('x')  # the possible variable names must be known beforehand...
        global f
        f = sympify(x1)
        xu = float(entry2.get())
        xl = float(entry3.get())
        global eps
        eps = float(entry4.get())
        bisection_method(xl, xu)

    button1 = Button(FalsePosition_window ,text='solve', command=solve_method, bg='#2873D8', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(400, 230, window=button1)

    # table
    my_table = ttk.Treeview(FalsePosition_window)
    my_table['columns'] = ('i', 'xl', 'f(xl)', 'xu', 'f(xu)', 'xr', 'f(xr)', 'Error')

    my_table.column("#0", width=0, stretch=NO)
    my_table.column("i", anchor=CENTER, width=80)
    my_table.column("xl", anchor=CENTER, width=100)
    my_table.column("f(xl)", anchor=CENTER, width=120)
    my_table.column("xu", anchor=CENTER, width=100)
    my_table.column("f(xu)", anchor=CENTER, width=120)
    my_table.column("xr", anchor=CENTER, width=100)
    my_table.column("f(xr)", anchor=CENTER, width=120)
    my_table.column("Error", anchor=CENTER, width=120)

    my_table.heading("#0", text="", anchor=CENTER)
    my_table.heading("i", text="I", anchor=CENTER)
    my_table.heading("xl", text="Xl", anchor=CENTER)
    my_table.heading("f(xl)", text="f(xl)", anchor=CENTER)
    my_table.heading("xu", text="Xu", anchor=CENTER)
    my_table.heading("f(xu)", text="f(xu)", anchor=CENTER)
    my_table.heading("xr", text="Xr", anchor=CENTER)
    my_table.heading("f(xr)", text="f(xr)", anchor=CENTER)
    my_table.heading("Error", text="Error", anchor=CENTER)
    canvas1.create_window(410, 400, window=my_table)

    def bisection_method(xl, xu):
        error = abs(xu - xl) * 100
        xr = 0
        step = 0
        if f.subs(x, xl) * f.subs(x, xu) >= 0:
            lable5 = Label(FalsePosition_window, text='no root or multiple roots present')
            canvas1.create_window(400, 400, window=lable5)
            quit()
        while error > eps:
            xrold = xr
            xr = xu - ((f.subs(x, xu) * (xl - xu)) / (f.subs(x, xl) - f.subs(x, xu)))
            error = abs((xr - xrold) / xr) * 100
            if step == 0:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, xl, f.subs(x, xl), xu, f.subs(x, xu), xr, f.subs(x, xr), "-"))
            else:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, xl, f.subs(x, xl), xu, f.subs(x, xu), xr, f.subs(x, xr), error))
            step = step + 1
            if f.subs(x, xr) * f.subs(x, xl) < 0:
                xu = xr
            elif f.subs(x, xr) * f.subs(x, xu) < 0:
                xl = xr
            else:
                quit()
        printroot(xr)


    def printroot(xr):

        rootlabel = Label(FalsePosition_window, text="Root=")  # shows as text in the window
        rootlabel.config(font=('sans-serif', 10))
        canvas1.create_window(540, 230, window=rootlabel)
        root = Label(FalsePosition_window, text=xr)  # shows as text in the window
        root.config(font=('sans-serif', 10))
        canvas1.create_window(620, 230, window=root)



    FalsePosition_window.mainloop()
def newton():
    # create window
    newton_window = Tk()
    newton_window.title('Newton Method')
    canvas1 = Canvas(newton_window, width=800, height=400, relief='raised')
    canvas1.pack()

    label1 = Label(newton_window, text='Enter function ( f(x) ) : ')
    label1.config(font=('sans-serif', 10))
    canvas1.create_window(130, 80, window=label1)
    entry1 = Entry(newton_window)
    canvas1.create_window(270, 80, window=entry1)

    # equation g(x)
    label2 = Label(newton_window, text='Enter function ( g(x) ) : ')
    label2.config(font=('sans-serif', 10))
    canvas1.create_window(450, 80, window=label2)
    entry2 = Entry(newton_window)
    canvas1.create_window(600, 80, window=entry2)

    # xi
    label3 = Label(newton_window, text='Xi:')
    label3.config(font=('sans-serif', 10))
    canvas1.create_window(200, 150, window=label3)
    entry3 = Entry(newton_window)
    canvas1.create_window(300, 150, window=entry3)

    # Error
    label4 = Label(newton_window, text='Error:')
    label4.config(font=('sans-serif', 10))
    canvas1.create_window(480, 150, window=label4)
    entry4 = Entry(newton_window)
    canvas1.create_window(580, 150, window=entry4)

    def solve_method():
        x1 = entry1.get()
        x2 = entry2.get()
        global x
        x = var('x')  # the possible variable names must be known beforehand...
        global f
        global g
        f = sympify(x1)
        g = sympify(x2)
        xi = float(entry3.get())
        global eps
        eps = float(entry4.get())
        newton_method(xi)

    button1 = Button(newton_window,text='solve', command=solve_method, bg='#2873D8', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(400, 200, window=button1)
    # table
    my_table = ttk.Treeview(newton_window)
    my_table['columns'] = ('i', 'xi', 'f(xi)', "f'(xi)", 'Error')

    my_table.column("#0", width=0, stretch=NO)
    my_table.column("i", anchor=CENTER, width=80)
    my_table.column("xi", anchor=CENTER, width=100)
    my_table.column("f(xi)", anchor=CENTER, width=120)
    my_table.column("f'(xi)", anchor=CENTER, width=120)
    my_table.column("Error", anchor=CENTER, width=120)

    my_table.heading("#0", text="", anchor=CENTER)
    my_table.heading("i", text="I", anchor=CENTER)
    my_table.heading("xi", text="Xi", anchor=CENTER)
    my_table.heading("f(xi)", text="f(Xi)", anchor=CENTER)
    my_table.heading("f'(xi)", text="f'(xi)", anchor=CENTER)
    my_table.heading("Error", text="Error", anchor=CENTER)
    canvas1.create_window(410, 350, window=my_table)

    def newton_method(xi):
        step = 0
        condition = True
        while condition:
            xiplus1 = xi-(f.subs(x, xi)/g.subs(x, xi))
            if step == 0:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, xi, f.subs(x, xi), g.subs(x, xi), "-"))
                error = abs((xiplus1 - xi) / xiplus1) * 100
            else:
                my_table.insert(parent='', index='end', iid=step, text='',
                                values=(step, xi, f.subs(x, xi), g.subs(x, xi), error))
                print(f.subs(x, xi))
            condition = error > eps
            error = abs((xiplus1 - xi) / xiplus1) * 100
            if error < eps:
                rootlabel = Label(newton_window, text="Root=")  # shows as text in the window
                rootlabel.config(font=('sans-serif', 10))
                canvas1.create_window(540, 200, window=rootlabel)
                root = Label(newton_window, text=xi)  # shows as text in the window
                root.config(font=('sans-serif', 10))
                canvas1.create_window(620, 200, window=root)
            step = step + 1
            xi = xiplus1
    newton_window.mainloop()
def goldenmax():
    goldenmax_window = Tk()
    goldenmax_window.title('Golden Method for max point')
    canvas1 = Canvas(goldenmax_window, width=800, height=400, relief='raised')
    canvas1.pack()

    # equation
    label1 = Label(goldenmax_window, text='Enter function ( f(x) ) : ')
    label1.config(font=('sans-serif', 10))
    canvas1.create_window(300, 80, window=label1)
    entry1 = Entry(goldenmax_window)
    canvas1.create_window(430, 80, window=entry1)

    # Xu
    label2 = Label(goldenmax_window, text='Xu:')
    label2.config(font=('sans-serif', 10))
    canvas1.create_window(140, 150, window=label2)
    entry2 = Entry(goldenmax_window)
    canvas1.create_window(220, 150, window=entry2)

    # Xl
    label3 = Label(goldenmax_window, text='Xl:')
    label3.config(font=('sans-serif', 10))
    canvas1.create_window(340, 150, window=label3)
    entry3 = Entry(goldenmax_window)
    canvas1.create_window(420, 150, window=entry3)

    # iteration
    label4 = Label(goldenmax_window, text='Iteration:')
    label4.config(font=('sans-serif', 10))
    canvas1.create_window(540, 150, window=label4)
    entry4 = Entry(goldenmax_window)
    canvas1.create_window(640, 150, window=entry4)

    def solve_method():
        x1 = entry1.get()
        global x
        x = var('x')  # the possible variable names must be known beforehand...
        global f
        f = sympify(x1)
        xu = float(entry2.get())
        xl = float(entry3.get())
        global itr
        itr = float(entry4.get())
        golden_method(xl, xu, itr)

    button1 = Button(goldenmax_window, text='solve', command=solve_method, bg='#2873D8', fg='white',
                     font=('helvetica', 9, 'bold'))
    canvas1.create_window(400, 230, window=button1)

    # table
    my_table = ttk.Treeview(goldenmax_window)
    my_table['columns'] = ('i', 'xl', 'f(xl)', 'x2', 'f(x2)', 'x1', 'f(x1)', 'xu', 'f(xu)', 'd')

    my_table.column("#0", width=0, stretch=NO)
    my_table.column("i", anchor=CENTER, width=80)
    my_table.column("xl", anchor=CENTER, width=100)
    my_table.column("f(xl)", anchor=CENTER, width=120)
    my_table.column("x2", anchor=CENTER, width=100)
    my_table.column("f(x2)", anchor=CENTER, width=120)
    my_table.column("x1", anchor=CENTER, width=100)
    my_table.column("f(x1)", anchor=CENTER, width=120)
    my_table.column("xu", anchor=CENTER, width=100)
    my_table.column("f(xu)", anchor=CENTER, width=120)
    my_table.column("d", anchor=CENTER, width=120)

    my_table.heading("#0", text="", anchor=CENTER)
    my_table.heading("i", text="I", anchor=CENTER)
    my_table.heading("xl", text="Xl", anchor=CENTER)
    my_table.heading("f(xl)", text="f(xl)", anchor=CENTER)
    my_table.heading("x2", text="X2", anchor=CENTER)
    my_table.heading("f(x2)", text="f(x2)", anchor=CENTER)
    my_table.heading("x1", text="X1", anchor=CENTER)
    my_table.heading("f(x1)", text="f(x1)", anchor=CENTER)
    my_table.heading("xu", text="Xu", anchor=CENTER)
    my_table.heading("f(xu)", text="f(xu)", anchor=CENTER)
    my_table.heading("d", text="d", anchor=CENTER)
    canvas1.create_window(410, 400, window=my_table)

    def golden_method(xl, xu, itr):
        step = 0
        while step < itr:

            d = 0.618 * (xu - xl)
            x1 = xl + d
            x2 = xu - d
            my_table.insert(parent='', index='end', iid=step, text='',
                            values=(
                                step, xl, f.subs(x, xl), x2, f.subs(x, x2), x1, f.subs(x, x1), xu, f.subs(x, xu), d))
            step = step + 1
            if f.subs(x, x2) > f.subs(x, x1):
                xu = x1
            if f.subs(x, x1) > f.subs(x, x2):
                xl = x2


    goldenmax_window.mainloop()
def goldenmin():
    goldenmin_window = Tk()
    goldenmin_window.title('Golden Method for min point')
    canvas1 = Canvas(goldenmin_window, width=800, height=400, relief='raised')
    canvas1.pack()

    # equation
    label1 = Label(goldenmin_window, text='Enter function ( f(x) ) : ')
    label1.config(font=('sans-serif', 10))
    canvas1.create_window(300, 80, window=label1)
    entry1 = Entry(goldenmin_window)
    canvas1.create_window(430, 80, window=entry1)

    # Xu
    label2 = Label(goldenmin_window, text='Xu:')
    label2.config(font=('sans-serif', 10))
    canvas1.create_window(140, 150, window=label2)
    entry2 = Entry(goldenmin_window)
    canvas1.create_window(220, 150, window=entry2)

    # Xl
    label3 = Label(goldenmin_window, text='Xl:')
    label3.config(font=('sans-serif', 10))
    canvas1.create_window(340, 150, window=label3)
    entry3 = Entry(goldenmin_window)
    canvas1.create_window(420, 150, window=entry3)

    # iteration
    label4 = Label(goldenmin_window, text='Iteration:')
    label4.config(font=('sans-serif', 10))
    canvas1.create_window(540, 150, window=label4)
    entry4 = Entry(goldenmin_window)
    canvas1.create_window(640, 150, window=entry4)

    def solve_method():
        x1 = entry1.get()
        global x
        x = var('x')  # the possible variable names must be known beforehand...
        global f
        f = sympify(x1)
        xu = float(entry2.get())
        xl = float(entry3.get())
        global itr
        itr = float(entry4.get())
        goldenmin_method(xl, xu, itr)

    button1 = Button(goldenmin_window, text='solve', command=solve_method, bg='#2873D8', fg='white',
                     font=('helvetica', 9, 'bold'))
    canvas1.create_window(400, 230, window=button1)

    # table
    my_table = ttk.Treeview(goldenmin_window)
    my_table['columns'] = ('i', 'xl', 'f(xl)', 'x2', 'f(x2)', 'x1', 'f(x1)', 'xu', 'f(xu)', 'd')

    my_table.column("#0", width=0, stretch=NO)
    my_table.column("i", anchor=CENTER, width=80)
    my_table.column("xl", anchor=CENTER, width=100)
    my_table.column("f(xl)", anchor=CENTER, width=120)
    my_table.column("x2", anchor=CENTER, width=100)
    my_table.column("f(x2)", anchor=CENTER, width=120)
    my_table.column("x1", anchor=CENTER, width=100)
    my_table.column("f(x1)", anchor=CENTER, width=120)
    my_table.column("xu", anchor=CENTER, width=100)
    my_table.column("f(xu)", anchor=CENTER, width=120)
    my_table.column("d", anchor=CENTER, width=120)

    my_table.heading("#0", text="", anchor=CENTER)
    my_table.heading("i", text="I", anchor=CENTER)
    my_table.heading("xl", text="Xl", anchor=CENTER)
    my_table.heading("f(xl)", text="f(xl)", anchor=CENTER)
    my_table.heading("x2", text="X2", anchor=CENTER)
    my_table.heading("f(x2)", text="f(x2)", anchor=CENTER)
    my_table.heading("x1", text="X1", anchor=CENTER)
    my_table.heading("f(x1)", text="f(x1)", anchor=CENTER)
    my_table.heading("xu", text="Xu", anchor=CENTER)
    my_table.heading("f(xu)", text="f(xu)", anchor=CENTER)
    my_table.heading("d", text="d", anchor=CENTER)
    canvas1.create_window(410, 400, window=my_table)

    def goldenmin_method(xl, xu, itr):
        step = 0
        while step < itr:

            d = 0.618 * (xu - xl)
            x1 = xl + d
            x2 = xu - d
            my_table.insert(parent='', index='end', iid=step, text='',
                            values=(
                                step, xl, f.subs(x, xl), x2, f.subs(x, x2), x1, f.subs(x, x1), xu, f.subs(x, xu), d))
            step = step + 1
            if f.subs(x, x2) > f.subs(x, x1):
                x2 = xl
            if f.subs(x, x1) > f.subs(x, x2):
                xu = x1


    goldenmin_window.mainloop()
def ludec():
    # create window
    LU_window = Tk()
    LU_window.title('LU Method')
    canvas1 = Canvas(LU_window, width=800, height=400, relief='raised')
    canvas1.pack()
    # create frane for user input
    matrixFrame = Frame(LU_window)
    canvas1.create_window(400, 130, window=matrixFrame)
    all_entries = []
    rows = 3
    cols = 4

    label1 = Label(LU_window, text='x1')
    label1.config(font=('sans-serif', 10))
    canvas1.create_window(320, 80, window=label1)
    label2 = Label(LU_window, text='x2')
    label2.config(font=('sans-serif', 10))
    canvas1.create_window(370, 80, window=label2)
    label3 = Label(LU_window, text='x3')
    label3.config(font=('sans-serif', 10))
    canvas1.create_window(420, 80, window=label3)
    label4 = Label(LU_window, text='b')
    label4.config(font=('sans-serif', 10))
    canvas1.create_window(470, 80, window=label4)
    global lmax
    lmax = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    # creates grid view for matrix
    for r in range(rows):
        entries_row = []
        for c in range(cols):
            e = Entry(matrixFrame, width=8)  # 5 chars
            e.insert('end', 0)
            e.grid(row=r, column=c)
            entries_row.append(e)
        all_entries.append(entries_row)

    # gets input for user and insert it into matrix
    def enter():
        # fill matrix with 0
        matrix = np.zeros((rows, cols))
        # insert values in matrix
        for r, row in enumerate(all_entries):
            for c, entry in enumerate(row):
                text = entry.get()
                matrix[r, c] = float(text)
        b = []
        b = [matrix[0, 3], matrix[1, 3], matrix[2, 3]]
        # make the upper triangle = 0 and fill l matrix
        umax = matrix
        for i in range(rows):
            if umax[i][i] == 0.0:
                print("no")
            for j in range(rows):
                if i != j and i < j:
                    ratio = umax[j][i] / umax[i][i]
                    lmax[j][i] = umax[j][i] / umax[i][i]
                    for k in range(cols):
                        umax[j][k] = umax[j][k] - ratio * umax[i][k]

        # sub for lc =b  and print C result on screen
        c1 = b[0]
        c2 = (b[1] - (lmax[1][0] * c1)) / lmax[1][1]
        c3 = (b[2] - (lmax[2][0] * c1 + lmax[2][1] * c2)) / lmax[2][2]
        Cresult = " "
        Cresult = ('  C1= %0.2f' % (c1)) + Cresult
        Cresult = ('  C2= %0.2f' % (c2)) + Cresult
        Cresult = ('  C3= %0.2f' % (c3)) + Cresult
        label2 = Label(LU_window, text='LC=b ')
        label2.config(font=('sans-serif', 13))
        canvas1.create_window(280, 270, window=label2)
        label1 = Label(LU_window, text=Cresult)
        label1.config(font=('sans-serif', 10))
        canvas1.create_window(320, 300, window=label1)
        # back sub and print X result on screen
        x3 = c3 / umax[2][2]
        x2 = (c2 - (umax[1][2] * x3)) / umax[1][1]
        x1 = (c1 - ((umax[0][1] * x2) + (umax[0][2] * x3))) / umax[0][0]
        Xresult = " "
        Xresult = ('  X1= %0.2f' % (x1)) + Xresult
        Xresult = ('  X2= %0.2f' % (x2)) + Xresult
        Xresult = ('  X3= %0.2f' % (x3)) + Xresult
        label2 = Label(LU_window, text='UX=C')
        label2.config(font=('sans-serif', 13))
        canvas1.create_window(280, 340, window=label2)
        label1 = Label(LU_window, text=Xresult)
        label1.config(font=('sans-serif', 10))
        canvas1.create_window(320, 370, window=label1)

    enterbtn = Button(LU_window, text='Enter Matrix', command=enter)
    canvas1.create_window(390, 200, window=enterbtn)

    LU_window.mainloop()
def cramers():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(ws)

    # sets the title of the
    # Toplevel widget
    newWindow.title("Cramers Rule")

    # sets the geometry of toplevel
    newWindow.geometry("700x450")

    # A Label widget to show in toplevel
    Label(newWindow,
          text="Cramers Rule").pack()
def gaus():
    # create window
    gauss_window = Tk()
    gauss_window.title('Gauss-Jordan Elimination Method')
    canvas1 = Canvas(gauss_window, width=800, height=400, relief='raised')
    canvas1.pack()
    # create frane for user input
    matrixFrame = Frame(gauss_window)
    canvas1.create_window(400, 130, window=matrixFrame)
    # labels for entry
    label1 = Label(gauss_window, text='x1')
    label1.config(font=('sans-serif', 10))
    canvas1.create_window(320, 80, window=label1)
    label2 = Label(gauss_window, text='x2')
    label2.config(font=('sans-serif', 10))
    canvas1.create_window(370, 80, window=label2)
    label3 = Label(gauss_window, text='x3')
    label3.config(font=('sans-serif', 10))
    canvas1.create_window(420, 80, window=label3)
    label4 = Label(gauss_window, text='b')
    label4.config(font=('sans-serif', 10))
    canvas1.create_window(470, 80, window=label4)
    all_entries = []
    rows = 3
    cols = 4

    # creates grid view for matrix
    for r in range(rows):
        entries_row = []
        for c in range(cols):
            e = Entry(matrixFrame, width=8)  # 5 chars
            e.insert('end', 0)
            e.grid(row=r, column=c)
            entries_row.append(e)
        all_entries.append(entries_row)

    # gets input for user and insert it into matrix
    def enter():
        # fill matrix with 0
        matrix = np.zeros((rows, cols))
        # insert values in matrix
        for r, row in enumerate(all_entries):
            for c, entry in enumerate(row):
                text = entry.get()
                matrix[r, c] = float(text)
        # make the upper triangle = 0
        gmax = matrix
        for i in range(rows):
            if gmax[i, i] == 0.0:
                print("no")
            for j in range(rows):
                if i != j and i < j:
                    ratio = gmax[j, i] / gmax[i, i]
                    for k in range(cols):
                        gmax[j, k] = gmax[j, k] - ratio * gmax[i, k]
        # back sub and print result on screen
        x3 = gmax[2, 3] / gmax[2, 2]
        x2 = (gmax[1, 3] - (gmax[1, 2] * x3)) / gmax[1][1]
        x1 = (gmax[0, 3] - ((gmax[0, 1] * x2) + (gmax[0, 2] * x3))) / gmax[0, 0]
        result = " "
        result = ('  X1= %0.2f' % x1) + result
        result = ('  X2= %0.2f' % x2) + result
        result = ('  X3= %0.2f' % x3) + result
        label2 = Label(gauss_window, text='Answer')
        label2.config(font=('sans-serif', 13))
        canvas1.create_window(280, 270, window=label2)
        label1 = Label(gauss_window, text=result)
        label1.config(font=('sans-serif', 10))
        canvas1.create_window(320, 300, window=label1)

    enterbtn = Button(gauss_window, text='Enter Matrix', command=enter)
    canvas1.create_window(390, 200, window=enterbtn)

    gauss_window.mainloop()
def functions():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(ws)

    # sets the title of the
    # Toplevel widget
    newWindow.title("Functions")

    # sets the geometry of toplevel
    newWindow.geometry("700x450")

    # A Label widget to show in toplevel
    Label(newWindow, text="Functions").pack()
    buttonsec = Button(newWindow , text='  Secant ',relief=RAISED,font=('Arial Bold', 18),bg="blue",
                       fg="white", activebackground="red", activeforeground="black", borderwidth=2, command=secant )
    buttonsec.place(x=200, y=150)

    buttonbis = Button(newWindow,text='   Bisection   ', relief=RAISED,  font=('Arial Bold', 18), bg="blue",
                       fg="white", activebackground="red", activeforeground="black", borderwidth=2, command=bisection)
    buttonbis.place(x=350, y=150)

    buttonsimp = Button(newWindow ,text='  Simple Fixed Point ',  relief=RAISED,   font=('Arial Bold', 18),  bg="blue",
                        fg="white", activebackground="red", activeforeground="black", borderwidth=2, command=simple)
    buttonsimp.place(x=550, y=150)

    buttonnew = Button(newWindow, text='Newton  ',  relief=RAISED, font=('Arial Bold', 18),  bg="blue", fg="white",
                       activebackground="red", activeforeground="black", borderwidth=2, command=newton)
    buttonnew.place(x=200, y=250)

    buttonfal = Button(newWindow, text='False position', relief=RAISED, font=('Arial Bold', 18),  bg="blue", fg="white",
                       activebackground="red", activeforeground="black", borderwidth=2, command=falsepos)
    buttonfal.place(x=350, y=250)
    buttongoldmax = Button(newWindow, text='Golden for max point ', relief=RAISED, font=('Arial Bold', 18), bg="blue",
                        fg="white", activebackground="red", activeforeground="black", borderwidth=2, command=goldenmax)
    buttongoldmax.place(x=550, y=250)
    buttongoldmin = Button(newWindow, text='Golden for min point ', relief=RAISED, font=('Arial Bold', 18), bg="blue",
                           fg="white", activebackground="red", activeforeground="black", borderwidth=2,
                           command=goldenmin)
    buttongoldmin.place(x=200, y=350)
def matrices():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(ws)

    # sets the title of the
    # Toplevel widget
    newWindow.title("Matrices")

    # sets the geometry of toplevel
    newWindow.geometry("700x450")

    # A Label widget to show in toplevel
    Label(newWindow, text="matrices").pack()
    button = Button(
        newWindow ,
        text='Gaussian elimination',
        relief=RAISED,
        font=('Arial Bold', 18),
        bg="blue", fg="white", activebackground="red", activeforeground="black", borderwidth=2, command=gaus
    )
    button.place(x=350, y=250)

    button = Button(
        newWindow ,
        text=' Cramers rule',
        relief=RAISED,
        font=('Arial Bold', 18),
        bg="blue", fg="white", activebackground="red", activeforeground="black", borderwidth=2, command=cramers
    )
    button.place(x=350, y=350)
    button = Button(
        newWindow ,
        text='  LU decomposition   ',
        relief=RAISED,
        font=('Arial Bold', 18),
        bg="blue", fg="white", activebackground="red", activeforeground="black", borderwidth=2, command=ludec
    )
    button.place(x=550, y=350)

buttonfunc=Button(
    ws, text='Functions', relief=RAISED,font=('Arial Bold', 18),
    bg="blue", fg="white", activebackground="red", activeforeground="black", borderwidth=2, command=functions,
)
buttonfunc.place(x=450, y=350)
buttonmat = Button(
    ws,text='Matrices', relief=RAISED,font=('Arial Bold', 18),
    bg="blue", fg="white", activebackground="red", activeforeground="black", borderwidth=2, command=matrices
)
buttonmat.place(x=650, y=350)
ws.mainloop()