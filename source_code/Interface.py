from source_code.database_operation import *
from source_code.Auth import *
from source_code.User_data import *
import gradio as gr

array = load_data()
Level = User_Level(array[0],array[1])
Username = Name_account(array[0],array[1])

def game_interface(Game_Name):
    game_id = find_game_id(array[0],Game_Name)
    price = fetch_one_game(game_id)
    link = badgelinkbuilder(array[2],game_id)
    output = f"The total Price of the set is : ${price}\n\nThe link for crafting this badge is this:              {link}"

    return output

def user_information_function():
    info_text = f"""
    Welcome {Username}
    
    Your current stats are:

    * Level : {Level}
    * Cooldown for obtaining booster pack:         {cooldown(Level)} Hours /  {(cooldown(Level))/24} Days
    * Your booster droprate for each game is:      {drop_rate(Level)} %

    The Cooldown serves as a minimum waiting time for you to drop a booster pack, then it will take its time based on your level and the number of games you own.

    in order for a booster pack to drop, you have to wait for someone to craft the set to level up that specific game you have, and you also need to have obtained all available cards from that game, usually equaling the lower half.
        
    """
    return info_text

def user_information_function2(Target_Level):
    Target_Level = int(Target_Level)
    C = cooldown(Target_Level)
    D = drop_rate(Target_Level)
    E = Exp_Calculator(Level, Target_Level)
    S = Sets_counts(E)

    info_text = f"""
    Target level = {int(Target_Level)}

    Your current stats are: 

    * Cooldown for obtaining booster pack:         {C} Hours / {C/24} Days
    * Your booster droprate for each game is:      {D} %

    You need [{E}] Exp for reaching this level  : i.e. [{S}] Sets.  
    
    All this costs approx $ {0.175 * S} Dollar

    #The Steam API does not allow you to check your current level experience
    """
    return info_text

def database(Quantative):
    adding_games(int(Quantative), array[0], array[2])
    return"Games Loaded in the Database"
    
def database2(Fetch_Set_Price):
    if Fetch_Set_Price == "YES":
        Done()
        return "Database Completed"
    
def image_exists():
    return ("https://i.imgur.com/H58XUIa.png")
    


steam_game_interface = gr.Interface(
        fn=game_interface,
        title = "Game information",
        description = "Input the game name to get all the information",
        inputs=["text"],
        outputs=["text"],
        )

image_interface = gr.Interface(
    fn=image_exists,
    inputs=None,
    outputs=gr.outputs.Image(type="pil", label="Author")
)
            
user_information_interface = gr.Interface(
        title = "User Information",
        description = "Click Generate to show all user's information in real time",
        fn=user_information_function,
        inputs=None,
        outputs=["text"],
        )

user_information_interface2 = gr.Interface(
        fn=user_information_function2,
        title = "Performance Comparison",
        description = "Add a level to view its stats and calculate the cost to level up, it should be higher than your actual level",
        inputs=["text"],
        outputs=["text"],
        )

database_interface = gr.Interface(
        fn=database,
        title = "Fetch Game Names",
        description = "Enter the number of games you want to upload to the database. [First Step]",
        inputs=["text"],
        outputs=["text"],
        )

database_interface2 = gr.Interface(
        fn=database2,
        title = "Fetch Game Set Price",
        description = "Write 'YES', if u want to start to Fetch Sets prices. [Second Step]",
        article = "The operation may take a while, since it depends on steam, you can make a maximum of 25 price requests in 200 seconds.    Even if the program crashes, the progress is saved",
        inputs=["text"],
        outputs=["text"],
        )
