import function
import PySimpleGUI as sg

label = sg.Txt("Type a to-do ")
input_box = sg.InputText(tooltip="Enter to-do")
add_button = sg.Button("Add")

window = sg.Window("My to do app",layout=[[label], [input_box, add_button]])

window.read()

window.close()