from tkinter import*

window=Tk()
window.title("Calculator Prorotype")
window.geometry("600x400")
window.iconbitmap("c:/Users/abhis/Downloads/calculator-48_45851.ico")

#data colllection
def find_sum():
    sum=int(n1.get()) + int(n2.get())
    result.set(sum) #sum result boxill varaan

result=StringVar()
#widgets
lb1=Label(window,text="Number 1")
lb2=Label(window,text="Number 2")
lb3=Label(window,text="Result")

n1=Entry(window)
n2=Entry(window)
n3=Entry(window,textvariable=result)
lb1.pack()
n1.pack()
lb2.pack()
n2.pack()
lb3.pack()
n3.pack()


#button
bt1=Button(window,text="find sum",command=find_sum)
bt1.pack()


window.mainloop()

