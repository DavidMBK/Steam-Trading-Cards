import os
import tkinter as tk
import webbrowser
import pandas as pd

def url1():
    webbrowser.open('https://steamcommunity.com/dev/apikey')

def url2():
    webbrowser.open('https://www.ubisoft.com/en-gb/help/article/finding-your-steam-id/000060565#:~:text=To%20view%20your%20Steam%20ID%3A&text=Select%20your%20Steam%20username.&text=Locate%20the%20URL%20field%20beneath,the%20end%20of%20the%20URL.')

def create_data():
    ApiKey = entry_ApiKey.get()
    SteamID = entry_SteamID.get()

    data = pd.DataFrame({'ApiKey': [ApiKey], 'SteamID': [SteamID]})
    parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    folder_path = os.path.join(parent_directory, 'User')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, 'Auth_token.csv')
    data.to_csv(file_path, mode='w', index=False)

    entry_ApiKey.delete(0, tk.END)
    entry_SteamID.delete(0, tk.END)

    root.destroy()

def Authy():
    global root, entry_ApiKey, entry_SteamID

    if not os.path.exists('User/Auth_token.csv'):
        root = tk.Tk()
        root.title("Auth Tokens")

        icon_file = "images/icon.ico"
        root.iconbitmap(icon_file)

        window_width = 300
        window_height = 150
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        label_ApiKey = tk.Label(root, text="API Key:")
        label_ApiKey.place(x=10, y=10)

        question_mark_image = tk.PhotoImage(file="images/question_mark.png")
        resized_question_mark_image = question_mark_image.subsample(30, 30)

        button_question_mark = tk.Button(root, image=resized_question_mark_image, command=url1)
        button_question_mark.image = resized_question_mark_image  
        button_question_mark.place(x=210, y=9)

        button_question_mark2 = tk.Button(root, image=resized_question_mark_image, command=url2)
        button_question_mark2.image = resized_question_mark_image 
        button_question_mark2.place(x=210, y=39)

        entry_ApiKey = tk.Entry(root)
        entry_ApiKey.place(x=80, y=10)

        label_SteamID = tk.Label(root, text="Steam ID:")
        label_SteamID.place(x=10, y=40)

        entry_SteamID = tk.Entry(root)
        entry_SteamID.place(x=80, y=40)
        
        button_save = tk.Button(root, text="Save", command=create_data)
        button_save.place(x=130, y=90)

        root.mainloop()

Authy()