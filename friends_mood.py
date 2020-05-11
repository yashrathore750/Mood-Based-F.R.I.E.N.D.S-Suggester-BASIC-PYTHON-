from tkinter import *
from tkinter import messagebox

root = Tk()

def Laugh():
    laugh = ['S01E07','S04E08','S04E12', 'S05E11','S05E14','S05E16', 'S06E11','S06E09','S06E17','S07E10','S07E11','S07E12','S10E03']
    messagebox.showinfo("Laughter", laugh)

def Cry():
    cry = ['S02E24','S03E16', 'S05E03','S06E24','S06E25','S09E21','S10E12', 'S10E16','S10E17','S10E18']
    messagebox.showinfo("Cry", cry)

def Smile():
    smile= ['S02E07','S02E12','S02E13','S02E14','S07E22','S08E23','S08E24']
    messagebox.showinfo("Smile", smile)

desc = Label(root, text="Hello! I am Bot. Depending on your mood I will suggest you episodes of 'Friends' ")
select_button = Label(root, text="Select the button associated with your mood ")
laugh_button = Button(root, text ="I want to laugh", command= Laugh)
cry_button = Button(root, text ="I want to cry",  command = Cry)
smile_button = Button(root, text ="I want to smile", command = Smile)

desc.pack()
select_button.pack()
laugh_button.pack()
cry_button.pack()
smile_button.pack()
#
# print("Depending on your mood I will suggest you episodes of 'Friends' ")
# print('Select number associated with your mood')
# mood = int(input('1. I want to laugh    '
#                  '2. I want to cry  '
#                  '3. I want to smile \n'))
#
# if(mood==1):
#     print("According to your selected mood. You can watch the following episodes :")
#     print(laugh)
# elif(mood == 2):
#     print("According to your selected mood. You can watch the following episodes :")
#     print(cry)
# elif(mood == 3):
#     print("According to your selected mood. You can watch the following episodes :")
#     print(smile)
# else:
#     print(" Error! You've Selected Number Apart from 1,2 & 3 ")

root.mainloop()
