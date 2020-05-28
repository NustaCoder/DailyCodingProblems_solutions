from tkinter import *
root = Tk()
root.title("Findyourcar.com")

label_head = Label(root, text= "select your brand here", padx= 20, pady= 10)
label_head.grid(row= 0, column=0, columnspan= 3)

current_car = StringVar()
carnames_list = ['bmw', 'audi', 'mercedes']
lst_bmw = [('bmw m8', '3.2 cr'), ('bmw m4', '78.24 lakh'), ('bmw x5', '82.24 lakh')]
lst_audi = [('audi R8', '3.2 cr'), ('audi A4', '78.24 lakh'), ('audi TT', '1.24 cr'), ('audi RS5', '1.7 cr')]
lst_mercedes = [('mercedes AMG GT', '2.27 CR'), ('mercedes GLA', '55.24 lakh')]

cnt = 1
lst = []
for i in carnames_list:
    Radiobutton(root, text= i, value= i, variable= current_car).grid(row= cnt, column= 0, sticky= "w")
    cnt += 1
def printname():
    global lst
    for i in lst:
        i.destroy()

    label_head = Label(root, text= "select your brand here", padx= 20, pady= 10)
    label_head.grid(row= 0, column=0, columnspan= 3)
    t = 1
    for i in carnames_list:
        Radiobutton(root, text= i, value= i, variable= current_car).grid(row= t, column= 0, sticky= "w")
        t += 1

    e = current_car.get()
    label_carname = Label(root, text= "name", padx= 10, pady= 10)
    label_carprice = Label(root, text= "price", padx= 10, pady= 10)
    label_carname.grid(row= 5, column= 0)
    label_carprice.grid(row= 5, column= 1)
    c = 6
    if e == 'bmw':
        for i, j in lst_bmw:
            Label(root, text=i, padx= 10, pady= 10).grid(row=c , column= 0, sticky= "w")
            Label(root, text=j, padx= 10, pady= 10).grid(row=c , column= 1, sticky= "w")
            c += 1
    elif e == 'audi':
        for i, j in lst_audi:
            Label(root, text=i, padx= 10, pady= 10).grid(row=c , column= 0, sticky= "w")
            Label(root, text=j, padx= 10, pady= 10).grid(row=c , column= 1, sticky= "w")
            c += 1
    elif e == 'mercedes':
        for i, j in lst_mercedes:
            Label(root, text=i, padx= 10, pady= 10).grid(row=c , column= 0, sticky= "w")
            Label(root, text=j, padx= 10, pady= 10).grid(row=c , column= 1, sticky= "w")
            c += 1
    btn_find = Button(root, text= "find cars", padx= 10, pady= 10, command= printname)
    btn_find.grid(row= cnt, column= 0)
        
    lst = root.grid_slaves()

btn_find = Button(root, text= "find cars", padx= 10, pady= 10, command= printname)
btn_find.grid(row= cnt, column= 0)


root.mainloop()
