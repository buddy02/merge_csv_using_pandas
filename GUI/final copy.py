import pandas as pd
from tkinter import *
from tkinter import filedialog
root = Tk()
root.title("Files Merger")
root.geometry('580x420')
root.configure(bg='#333333')

frame = Frame(bg='#333333')

l1 = Label(frame, text="Let's Merge!", bg='#333333', fg='#FF3399', font=("Arial", 32))
l = Label(frame, text="Enter number of files: ", bg='#333333', fg='#FFFFFF', font=("Arial", 16))
e = Entry(frame, font=("Arial", 16))

l1.grid(row=0, column=0, columnspan=2, pady=40)
l.grid(row=1, column=0)
e.grid(row=1, column=1, pady=20)


li = []

# On clicking start button this function will run asking to add files
def nof(nf):
    n = (int)(e.get())
    for i in range(n):
        root.filename = filedialog.askopenfilename()
        df = pd.read_csv(root.filename)
        li.append(df)
    nf.grid_remove()
    b = Button(frame, text="Merge", bg='#FF3399', fg='#FFFFFF',padx=5, font=("Arial", 16), command=lambda: onclick(b))
    b.grid(row=3, columnspan=2, pady=20)

# On clicking merge button this function will run to merge uploaded files
def onclick(b):
    n = (int)(e.get())
    # To remove duplicates in file
    for i in range(n):
        li[i] = li[i].drop_duplicates(subset=['Controller_time'], keep='last')
    # To merge the files
    merged = pd.merge(li[0], li[1], on='Controller_time')
    for i in range(2, n):
        merged = pd.merge(merged, li[i], on='Controller_time')
    save = filedialog.asksaveasfilename(defaultextension=".csv")
    merged.to_csv(save, index=False)
    l2 = Label(frame, text="The files have been Merged", bg='#333333', fg='#FFFFFF', font=("Arial", 16))
    l2.grid(row=4, columnspan=2,  pady=10)
    b.grid_remove()


nf = Button(frame, text="Start", bg='#FF3399', fg='#FFFFFF',padx=12, font=("Arial", 16), command=lambda: nof(nf))
nf.grid(row=2, columnspan=2, pady=20)


frame.pack()

root.mainloop()
