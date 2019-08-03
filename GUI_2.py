import PySimpleGUI as sg
list1=[]
list2=[]
col = [
        [sg.Listbox(enable_events=True,values=list2, size=(30, 6),key="Lst2")],
        [sg.Button("ADD",key="Add")],
        [sg.Button("Complete",key="Com")],
        [sg.Button("DEL",key="Del")]
      ]
layout = [
        [sg.Listbox(enable_events=True,values=list1, size=(30, 6),key="Lst"),sg.Column(col)],
        [sg.Text('Enter your task'),sg.InputText("", key='task')],
        [sg.Button("Exit")]]
window = sg.Window('My first GUI', layout)
button, values = window.Read()

while True:
    button, values = window.Read()
    print(values,button)
    if button == "Add":
        list1.append(values['task'])
        window.FindElement('task').Update("")
        window.FindElement('Lst').Update(values=list1)
        window.FindElement('Add').Update('ADD')
    elif button=="Del":
        list1.remove("".join(values["Lst"][0]))
        window.FindElement('Lst').Update(values=list1)
    elif button == "Del":
        list2.remove("".join(values["Lst2"][0]))
        window.FindElement('Lst2').Update(values=list2)
    elif button=="Com":
        list2.append(values['Lst'][0])
        window.FindElement('Lst2').Update(values=list2)
        list1.remove(values['Lst'][0])
        window.FindElement('Lst').Update(values=list1)
        window.FindElement('Com').Update("Complete")
    elif button=="Exit":
        break

window.Close()