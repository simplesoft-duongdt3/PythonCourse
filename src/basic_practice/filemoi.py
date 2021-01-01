# from vietnam_number import w2n
# text = 'một triệu không trăm tám mươi lăm nghìn ba trăm ba mươi hai'
# a=w2n(text)
# print(a)

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello, World!"

import PySimpleGUI as sg

sg.theme('Topanga')      # Add some color to the window

# Very basic window.  Return values using auto numbered keys

layout = [
    [sg.Text('Please enter your Name, Address, Phone')],
    [sg.Text('Name', size=(15, 1)), sg.InputText()],
    [sg.Text('Address', size=(15, 1)), sg.InputText()],
    [sg.Text('Phone', size=(15, 1)), sg.InputText()], B  
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Simple data entry window', layout)
event, values = window.read()
window.close()
print(event, values[0], values[1], values[2])    # the input data looks like a simple list when auto numbered