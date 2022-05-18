import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("To-Do List") 

def add_task():
    pass

#creareGUI
listbox_task = tkinter.Listbox(root, height=3, width=50)
listbox_task.pack()

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text = "Add task", width = 48, command=add_task)
button_add_task.pack()


root.mainloop()
