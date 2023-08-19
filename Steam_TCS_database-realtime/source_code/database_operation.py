from steam import Steam
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import time
import matplotlib.pyplot as plt
from openpyxl import load_workbook

# -----------------------------------------------------------  Fetch Games Names --------------------------------------------------------------------

def get_all_steam_game_names(base_url, Q_G=0):
    game_names = []
    current_page = 1

    while True:
        url = f"{base_url}&page={current_page}"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            name_elements = soup.find_all("span", class_="title")

            if not name_elements:
                break  # Stop if no more game names found on the page

            for element in name_elements:
                game_name = element.text.strip()
                # Check if the game name is not already in the list before adding it
                if game_name not in game_names:
                    game_names.append(game_name)

                    if len(game_names) >= Q_G:
                        return game_names[:Q_G]
                    
            current_page += 1
        else:
            print(f"Error: Unable to fetch game names. Status Code: {response.status_code}")
            break

    return game_names

def database_games(games, AppID, Link, filename = 'Database.csv'):
    data = pd.DataFrame({"Game Name": games, "AppID": AppID,"Trading Cards Set cost": 0, "Currency = Dollar":'$', "Badge Link": Link})
    data.to_csv(filename, index=False)

def adding_games(Quantitive_games, apikey, urlid):
    game_names = get_all_steam_game_names("https://store.steampowered.com/search/?sort_by=Price_ASC&category1=998&category2=29&hidef2p=1&ndl=1", Quantitive_games)
    final_id = []
    final_link = []
    true_game = []
    if game_names:
        print(f"First {Quantitive_games} Steam game names:")
        for i, game_name in enumerate(game_names, start=1):
            AppID = find_game_id(apikey, game_name)
            if AppID == None:
                continue
            else:
                true_game.append(game_name)        
                Link = badgelinkbuilder(urlid, AppID)
                final_link.append(Link)
                final_id.append(AppID)
                print(f"{i}. {game_name} : {AppID}")
        database_games(true_game, final_id , final_link)
        print(f"Added {len(true_game)} games")
    else:
        print("No game names found.")
    return true_game



# -----------------------------------------------------------  Fetch Set Price --------------------------------------------------------------------

def trading_cards_url(app_id):
    url = f"https://steamcommunity.com/market/search?q=&category_753_Event%5B%5D=any&category_753_Game%5B%5D=tag_app_{app_id}&category_753_cardborder%5B%5D=tag_cardborder_0&appid=753"
    return url

def get_card_prices(app_id):

    game_url = trading_cards_url(app_id)
    response = requests.get(game_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        card_prices_normal = []

        cards = soup.find_all("span", class_="market_table_value normal_price")

        for card in cards:
            card_price_text = card.text.strip()
            price_match = re.search(r'\d+\.\d+', card_price_text)
            if price_match:
                price = float(price_match.group())
                card_prices_normal.append(price)

        return card_prices_normal

    else:
        print(f"Error: Unable to fetch card prices. Status Code: {response.status_code} - Wait 200 seconds")
        time.sleep(200)
        return []

def adding_sets_prices_database():
    count_errori = 0
    data = pd.read_csv('Database.csv')
    game_id = data['AppID']
    
    if data['Trading Cards Set cost'].eq(0).any():

        for i, game_id in enumerate(game_id, start=0):
            while True:
                card_prices = get_card_prices(game_id)
                if card_prices:
                    total_price = sum(card_prices)
                    data.at[i, 'Trading Cards Set cost'] = total_price  # Update the price in the DataFrame
                    data.sort_values(by='Trading Cards Set cost', ascending=True, inplace=True)
                    data.to_csv('Database.csv', index=False)
                    a = len(data[data['Trading Cards Set cost'] != 0].index)
                    print(f'Loaded games: {a}\n[L o a d i n g]')
                    time.sleep(2)
                    count_errori = 0
                    break
                else:
                    count_errori += 1
                    print(f"{game_id} didn't load.... I'll try again in 5 seconds : [{count_errori}/3]\nif it becomes 3/3 it will be deleted from the database and the program will go on with other games")
                    time.sleep(5)
                    if count_errori == 3:
                        count_errori = 0
                        data.drop(data[data['AppID'] == game_id].index, inplace=True)
                        data.to_csv('Database.csv', index=False)
                        game_id = data['AppID']  # Update the game_names list after removal
                        break
            if  not data['Trading Cards Set cost'].eq(0).any():
                return count_errori
    return count_errori

def fetch_one_game(game_name):
    card = get_card_prices(game_name)
    if card:
        set = sum(card)
    else:
        print("No cards found")
        
    return set


# -----------------------------------------------------------  Badge for Game --------------------------------------------------------------------

def badgelinkbuilder(urlid,game_id):
    url = f"https://steamcommunity.com/id/{urlid}/gamecards/{game_id}"
    return url

def find_game_id(api, game_name):
    steam = Steam(api)
    
    try:
        try:
            id = steam.apps.search_games(game_name)
            app_id = id['apps'][0]['id']
            return app_id
        except (ValueError, IndexError):
            return None
    except IndexError:
        game_name = game_name.replace(" ", "")
        id = steam.apps.search_games(game_name)
        app_id = id['apps'][0]['id']
        return app_id

#print(find_game_id("DaviD-GG","UBERMOSH + ORIGINAL SOUNDTRACK"))


# -----------------------------------------------------------  Completing the database with additions --------------------------------------------------------------------

def pdf():
    data = pd.read_csv('Database.csv')

    # Categorize the prices into different ranges
    price_ranges = {
        'Less than 20 cents': data[data['Trading Cards Set cost'] < 0.20].shape[0],
        '20 cents to 30 cents': data[(data['Trading Cards Set cost'] >= 0.20) & (data['Trading Cards Set cost'] < 0.30)].shape[0],
        '30 cents to 50 cents': data[(data['Trading Cards Set cost'] >= 0.30) & (data['Trading Cards Set cost'] < 0.50)].shape[0],
        '50 cents to 99 cents': data[(data['Trading Cards Set cost'] >= 0.50) & (data['Trading Cards Set cost'] < 0.99)].shape[0],
        'Greater than 1 dollar': data[data['Trading Cards Set cost'] >= 1].shape[0],
    }

    # Create the pie chart
    plt.figure(figsize=(8, 8))
    wedges, texts, autotexts = plt.pie(
        price_ranges.values(),
        labels=[f"{k} ({v})" if v > 0 else "" for k, v in price_ranges.items()],
        autopct=lambda pct: f'{pct:.1f}%' if pct > 0 else "",
        startangle=140
    )
    a = len(data[data['Game Name'] != 0].index)
    # Add title
    plt.title(f'Game set price distribution ({a})')

    # Move the legend outside of the pie chart
    plt.legend(wedges, price_ranges.keys(), title='Range', loc='center left', bbox_to_anchor=(1, 1, 0.5, 0))

    # Save the pie chart as a PDF
    plt.savefig('Database_pie_chart.pdf', bbox_inches='tight', dpi=300)

    # Show the plot (optional)
    #plt.show()


def creating_excel():
    data = pd.read_csv('Database.csv')
    data.to_excel('Database.xlsx', index=False)
    
    # Add distance for each column
    wb = load_workbook('Database.xlsx')
    ws = wb.active
    column_widths = {'A': 40, 'B': 15, 'C': 30, 'D':30, 'E':70}
    for column, width in column_widths.items():
        ws.column_dimensions[column].width = width

    wb.save('Database.xlsx')

def Done():
    adding_sets_prices_database()
    pdf()
    creating_excel()

