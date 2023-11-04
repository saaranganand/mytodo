import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

def get_theme(tasks):
    if tasks <= 5:
        return 'DarkGreen'
    elif tasks <= 10:
        return 'LightBrown9'
    else:
        return 'DarkRed2'

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key='todos', 
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
clear_button = sg.Button("Clear")
exit_button = sg.Button("Exit")

tasks = len(functions.get_todos())
sg.theme(get_theme(tasks))

window = sg.Window('My To-Do App', 
                   layout=[[clock],
                           [label], 
                           [input_box, add_button], 
                           [list_box, edit_button, complete_button],
                           [clear_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %y %H:%M:%S"))
    
    incomplete_tasks = len([task for task in functions.get_todos()])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please first select a todo", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please first select a todo", font=("Helvetica", 20))
        case "Clear":
            todos = functions.get_todos()
            todos.clear()
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()