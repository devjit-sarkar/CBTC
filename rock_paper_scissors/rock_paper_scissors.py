import tkinter
import os
import random

objects = {0:"rock",1:"paper",2:"scissors"}
winning = {"rock":"scissors","scissors":"paper","paper":"rock"}
losing = {"paper":"scissors","scissors":"rock","rock":"paper"}

def winner(player, photo):
    opponent = random.randint(0,2)

    rock_button.grid_forget()
    paper_button.grid_forget()
    scissors_button.grid_forget()

    if winning[player] == objects[opponent]:
        background = "#F9A930"
        result_label = tkinter.Label(text="You won!", font="comicsans 25 bold", bg= background)
    elif losing[player] == objects[opponent]:
        background = "#2BEDF7"
        result_label = tkinter.Label(text="You lost!", font="comicsans 25 bold", bg= background)
    else:
        background = "#61C9AC"
        result_label = tkinter.Label(text="Tied!", font="comicsans 25 bold", bg= background)

    #player's choice v/s system's choice
    outcome_label_you_chose = tkinter.Label(text="You chose:", font="comicsans 25 bold", fg="black", bg=background)
    outcome_label_system_chose = tkinter.Label(text=":System chose", font="comicsans 25 bold", fg="black", bg=background)
    
    system_choice_image_path = os.path.join(base_folder, f'{objects[opponent]}.png')
    system_choice_image = tkinter.PhotoImage(file=system_choice_image_path)

    player_choice = tkinter.Label(image=photo)
    system_choice = tkinter.Label(image=system_choice_image)

    result_label.pack(pady=30)

    outcome_label_you_chose.pack(padx=20,side="left")
    outcome_label_system_chose.pack(padx=10,side="right")
    player_choice.pack(side="left")
    system_choice.pack(side="right")

    # Keep a reference to the images to prevent garbage collection
    player_choice.image = photo
    system_choice.image = system_choice_image
  
    try_again_button = tkinter.Button(fg="black", bg=background,text="Try Again?", command=try_again, borderwidth=5)
    try_again_button.pack(pady=250)
    winner.outcome_widgets = [outcome_label_you_chose,outcome_label_system_chose, player_choice, system_choice, try_again_button, result_label]

def try_again():
    for widgets in winner.outcome_widgets:
        widgets.pack_forget()

    rock_button.grid(row=1,column=1,padx=75, pady=205, sticky = "NSEW")
    paper_button.grid(row=1,column=2,padx=75,pady=205, sticky = "NSEW")
    scissors_button.grid(row=1,column=3,padx=75,pady=205, sticky = "NSEW")

def input_rock():
    winner("rock", rock_photo)

def input_scissors():
    winner("scissors", scissors_photo)

def input_paper():
    winner("paper", paper_photo)

#setting base folder path for reference later on
base_folder = os.path.dirname(__file__)

root = tkinter.Tk()
root.title("Rock Paper Scissors")
root.geometry("1200x700")
root.resizable("false","false")

background_image_path = os.path.join(base_folder, 'background_image.png')
background_image = tkinter.PhotoImage(file =background_image_path )
background_image_label = tkinter.Label(root, image = background_image)
background_image_label.place(x=0, y=0)

rock_path = os.path.join(base_folder, 'rock.png')
rock_photo = tkinter.PhotoImage(file=rock_path)

scissors_path = os.path.join(base_folder, 'scissors.png')
scissors_photo = tkinter.PhotoImage(file=scissors_path)

paper_path = os.path.join(base_folder, 'paper.png')
paper_photo = tkinter.PhotoImage(file=paper_path)

tkinter.Grid.rowconfigure(root,1,weight=1)
tkinter.Grid.columnconfigure(root,1,weight=1)
tkinter.Grid.columnconfigure(root,2,weight=1)
tkinter.Grid.columnconfigure(root,3,weight=1)

rock_button = tkinter.Button(image=rock_photo, command=input_rock)
rock_button.grid(row=1,column=1,padx=75, pady=205, sticky = "NSEW")

paper_button = tkinter.Button(image=paper_photo, command=input_paper)
paper_button.grid(row=1,column=2,padx=75,pady=205, sticky = "NSEW")

scissors_button = tkinter.Button(image=scissors_photo, command=input_scissors)
scissors_button.grid(row=1,column=3,padx=75,pady=205, sticky = "NSEW")

root.mainloop()