import os
import webbrowser
app_input = input("What is the directory of the file you want to open?\n")
if app_input == "voxj":
    webbrowser.open_new_tab('https://voxj.github.io/')
else:
    os.system(app_input)
if app_input == "nggyu":
    webbrowser.open_new_tab('https://youtu.be/dQw4w9WgXcQ')
else:
    os.system(app_input)
