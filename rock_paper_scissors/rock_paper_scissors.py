import tkinter
import os


#image_path = os.path.join(base_folder, 'blueface.png')

#create a dictionary for values of Rock-Paper-Scissors
#-1 for rock, 0 for paper, 1 for scissors

#or scrap this plan and use strings
#p<r<s:values 
#paper beats rock, rock beats scissors, exception is paper is beaten by scissors
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


def input_rock():
    return

def input_scissors():
    return

def input_paper():
    return

def try_again():
    return

root = tkinter.Tk()

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

rock_button = tkinter.Button(root,image=rock_photo, command=input_rock, borderwidth=10)
rock_button.grid(row=1,column=1,padx=50, pady=150, sticky = "NSEW")

paper_button = tkinter.Button(image=paper_photo, command=input_paper, borderwidth=10)
paper_button.grid(row=1,column=2,padx=50,pady=150, sticky = "NSEW")

scissors_button = tkinter.Button(image=scissors_photo, command=input_scissors, borderwidth=10)
scissors_button.grid(row=1,column=3,padx=50,pady=150, sticky = "NSEW")

# try_again_button = tkinter.Button(text="Try Again?", command=try_again, borderwidth=5)
# try_again_button.grid(row = 5,sticky = "NSEW")

root.mainloop()