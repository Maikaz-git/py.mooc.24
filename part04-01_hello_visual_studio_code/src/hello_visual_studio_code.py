# Write your solution here

#/home/maik/.local/share/tmc/vscode/mooc-programming-24/part04-01_hello_visual_studio_code/src/hello_visual_studio_code.py


while True:
    editor = input("Which editor are you using: ").title()

    if editor == "Word" or editor == "Notepad":
        print("awful")
    elif editor == "Visual Studio Code":
        print("an excellent choice!")
        break
    else:
        print('not good')  
