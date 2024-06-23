import tkinter
import os
import random

#image_path = os.path.join(base_folder, 'blueface.png')

#create a dictionary for values of Rock-Paper-Scissors
#-1 for rock, 0 for paper, 1 for scissors

#or scrap this plan and use strings
#p<r<s:values 
#paper beats rock, rock beats scissors, exception is paper is beaten by scissors
objects = {0:"rock",1:"paper",2:"scissors"}
winning = {"rock":"scissors","scissors":"paper","paper":"rock"}
losing = {"paper":"scissors","scissors":"rock","rock":"paper"}

# def win(player_1, player_2):
#     if player_1 == player_2:
#         #return tie
#         return
#     elif player_1 < player_2:

# def player_input():
#     #take input from tkinter buttons
#     return #the input string

def winner(player, photo):
    opponent = random.randint(0,2)

    rock_button.grid_forget()
    paper_button.grid_forget()
    scissors_button.grid_forget()

    if winning[player] == objects[opponent]:
        #return "You win!"
        background = "#ADD899"
        root.configure(bg=background)
        result_label = tkinter.Label(text="You won!", font="comicsans 25 bold", bg= background)
        #result_label.pack(padx=90,pady=120)
    elif losing[player] == objects[opponent]:
        #return "You lost!"
        background = "#FF6969"
        root.configure(bg=background)
        result_label = tkinter.Label(text="You lost!", font="comicsans 25 bold", bg= background)
        #result_label.pack(padx=90,pady=120)
    else:
        #return "Tied!"
        background = "#A1D4B1"
        root.configure(bg=background)
        result_label = tkinter.Label(text="Tied!", font="comicsans 25 bold", bg= background)
        #result_label.pack(padx=90,pady=120)

    #player's choice v/s system's choice
    outcome_label = tkinter.Label(text="You chose:\t\tv/s\t\tSystem chose:", font="comicsans 25 bold", bg=background)
    outcome_label.pack(padx=50, pady=50)

    #player_choice_image = os.path.join(base_folder, f'{player}.png')
    system_choice_image_path = os.path.join(base_folder, f'{objects[opponent]}.png')
    #print(system_choice_image_path)
    system_choice_image = tkinter.PhotoImage(file=system_choice_image_path)

    player_choice = tkinter.Label(image=photo)
    system_choice = tkinter.Label(image=system_choice_image)

    player_choice.pack(side="left",padx=50, pady=60)
    system_choice.pack(side="right",padx=50, pady=60)

    # Keep a reference to the images to prevent garbage collection
    player_choice.image = photo
    system_choice.image = system_choice_image

    result_label.pack(padx=90,pady=120)

    try_again_button = tkinter.Button(text="Try Again?", command=try_again, borderwidth=5)
    #try_again_button.grid(row = 5,sticky = "NSEW")
    try_again_button.pack(padx=110,pady=120)
    winner.outcome_widgets = [outcome_label, player_choice, system_choice, try_again_button, result_label]

def try_again():
    for widgets in winner.outcome_widgets:
        widgets.pack_forget()

    rock_button.grid(row=1,column=1,padx=50, pady=150, sticky = "NSEW")
    paper_button.grid(row=1,column=2,padx=50,pady=150, sticky = "NSEW")
    scissors_button.grid(row=1,column=3,padx=50,pady=150, sticky = "NSEW")

def input_rock():
    outcome = winner("rock", rock_photo)
    #print(outcome)

def input_scissors():
    outcome = winner("scissors", scissors_photo)
    #print(outcome)

def input_paper():
    outcome = winner("paper", paper_photo)
    #print(outcome)

root = tkinter.Tk()
#insert title later on
base_folder = os.path.dirname(__file__)

root.geometry("1200x700")
root.resizable("false","false")
root.configure(bg="#A1D4B1")
#frame = tkinter.Frame(root, bg="#D9CAB3")
rock_path = os.path.join(base_folder, 'rock.png')
rock_photo = tkinter.PhotoImage(file=rock_path)

scissors_path = os.path.join(base_folder, 'scissors.png')
scissors_photo = tkinter.PhotoImage(file=scissors_path)

paper_path = os.path.join(base_folder, 'paper.png')
paper_photo = tkinter.PhotoImage(file=paper_path)

#have to change image resolution

#frame1 code
# frame1 = tkinter.Frame(root, borderwidth=10, relief="sunken")
# frame1.configure(bg="#E88D67")
# frame1.grid_columnconfigure(0, weight=1)
# frame1.grid_rowconfigure(0, weight=1)

tkinter.Grid.rowconfigure(root,1,weight=1)
tkinter.Grid.columnconfigure(root,1,weight=1)
tkinter.Grid.columnconfigure(root,2,weight=1)
tkinter.Grid.columnconfigure(root,3,weight=1)
#tkinter.Grid.rowconfigure(root,1,weight=1)

#frame1.pack()

rock_button = tkinter.Button(image=rock_photo, command=input_rock, borderwidth=10)
rock_button.grid(row=1,column=1,padx=50, pady=150, sticky = "NSEW")

paper_button = tkinter.Button(image=paper_photo, command=input_paper, borderwidth=10)
paper_button.grid(row=1,column=2,padx=50,pady=150, sticky = "NSEW")

scissors_button = tkinter.Button(image=scissors_photo, command=input_scissors, borderwidth=10)
scissors_button.grid(row=1,column=3,padx=50,pady=150, sticky = "NSEW")

# try_again_button = tkinter.Button(text="Try Again?", command=try_again, borderwidth=5)
# try_again_button.grid(row = 5,sticky = "NSEW")

root.mainloop()