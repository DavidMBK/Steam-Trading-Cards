from steam import Steam
import pandas as pd
import time
from urllib.parse import urlparse

def load_data():
    data = pd.read_csv('User/Auth_token.csv')
    ApiKey = data['ApiKey'][0]
    SteamID = data['SteamID'][0]

    steam = Steam(ApiKey)
    user = steam.users.get_user_details(SteamID)

    url = user['player']['profileurl']
    url = urlparse(url)
    url = url.path.strip("/")
    profile_url_id = url.split("/")[-1]

    list = [ApiKey, SteamID, profile_url_id]

    return list

def User_Level(ApiKey, SteamID):
    steam = Steam(ApiKey)
    time.sleep(1)
    response = steam.users.get_user_steam_level(SteamID)
    #print(response)
    player_level = response['player_level']
    return player_level

def Exp_Calculator(Current_level, Target_level, exp=0):
    exp_gap = 1
    i = 1
    while Current_level != Target_level:
        if (Current_level == i):
            exp += (100 * exp_gap)
            Current_level += 1
        else:
            i+= 1
            if(i % 10 == 0):
                exp_gap +=1
    exp = round(exp/100)
    return exp * 100         

def Sets_counts(exp):
    return exp / 100

def drop_rate(level):
    return ((20 * (int(level / 10))) / 100) + 1

def cooldown(level):
    return (14*24)/(1+(level/50))

def Name_account(ApiKey, SteamID):
    steam = Steam(ApiKey)
    response = steam.users.get_user_details(SteamID)
    #print(response)
    player_name = response['player']['personaname']
    return player_name
