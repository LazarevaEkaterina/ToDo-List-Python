'''
To-do list application
python 3.10.4

Making a small project to try tkinter gui and pickle save and load data

'''

import tkinter
from tkinter import messagebox as tkmsgbox
import pickle

root = tkinter.Tk()
root.title("To-Do List") 

def add_task() -> None:
    '''
    Get text from element entry_task and insert into element listbox_tasks
    
    Input: None
    Return: None
    '''
    task = entry_task.get()
    if task == "":
        tkmsgbox.showwarning(title = "Warning!", message="You must enter a task")
        return

    listbox_tasks.insert(tkinter.END, task)
    entry_task.delete(0, tkinter.END)

def delete_task() -> None:
    '''
    Delete current selection from listbox_tasks
    
    Input: None
    Return: None
    '''
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkmsgbox.showwarning(
            title = "Warning!", 
            message="You must select a task"
        )


def load_tasks() -> None:
    '''
    Trying to find tasks.dat file in active directory

    If file exists and it's not empty -> pickle.load returns 
    list of str and insert it to listbox_tasks 
        (removing existed data in listbox_tasks)

    If file not exist throw tkinter massagebox warning!

    Input: None
    Rerurn: None
    '''
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
    except:
        tkmsgbox.showwarning(
            title = "Warning!", 
            message="Cannot find tasks.dat. Maybe you didn't save any of your tasks earlier"
        )
    if len(tasks) == 0:
        tkmsgbox.showwarning(
            title = "Warning!", 
            message="Empty tasks.dat file. Nothing to show"
        )
        return

    listbox_tasks.delete(0, tkinter.END)
    for task in tasks:
        listbox_tasks.insert(tkinter.END, task)

def save_tasks():
    '''
    Trying to save list of notes to tasks.dat file into active directory
    
    If listbox_tasks is empty -> throw tkinter warning of empty list

    pickle saves data into dat file. It's easier to deploy and recovering data.

    Input: None
    Rerurn: None
    '''
    if listbox_tasks.size() == 0:
        tkmsgbox.showwarning(
            title = 'Warning!',
            message='Nothing to save! Make at least one To-do note.'
        )
        return

    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))
    tkmsgbox.showinfo(
        title="Success",
        message='Successfully created file tasks.dat!'
    )


#creareGUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=20, width=50)
listbox_tasks.pack(side = tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side = tkinter.RIGHT, fill = tkinter.Y)

# scrollbar_tasks.config(yscrollcommand = scrollbar_tasks.set)
# scrollbar_tasks.config(command = listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", width=50, command=add_task)
button_delete_task = tkinter.Button(root, text="Delete task", width=50, command=delete_task)
frame_load_save_data = tkinter.Frame(root)
button_load_tasks = tkinter.Button(root, text="Load tasks", width=25, command=load_tasks)
button_save_tasks = tkinter.Button(root, text="Save tasks", width=25, command=save_tasks)


button_add_task.pack()
button_delete_task.pack()
frame_load_save_data.pack()
button_load_tasks.pack(side=tkinter.LEFT)
button_save_tasks.pack(side=tkinter.RIGHT)

root.mainloop()
