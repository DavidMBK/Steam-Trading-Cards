# Steam Trading Cards Information
This project is primarily dedicated to individuals who are looking to level up on a budget.

By following a few simple steps, this program efficiently identifies the most cost-effective card sets in ascending order of price.

This functionality is especially valuable as it allows you to spend less on leveling sets within Steam compared to third-party services. While these services may offer speed and efficiency, they often charge more for the cards.

Additionally, you can verify the cooldown period for receiving card packs and the relevant drop rate.

## Key Features

- Generate a dataset of games with lower costs during that time period.
- Find real-time prices of cards from the dataset of games created.
- Incorporate the badge link for every game in the Excel file database.
- Examine the card set of a specific game.
- Perform an analysis of the cost of leveling up a Steam player using real-time data, reviewing relevant statistics for that level.


## Game Information Retrieval
You can input the game's name and retrieve one of the following types of information.

![](https://i.imgur.com/IYoh6im.png)



## Dataset

This section enables you to compile a dataset of games that begin with the lowest price on Steam (and have card sets available). It also provides the ability to review set prices for all the games imported in the initial phase.

![](https://i.imgur.com/huOxBT5.png)

Once the Fetch Game Set Price operation is complete, the program will generate a pie chart in PDF format to visualize the discovered prices and an Excel file for a more comprehensive overview.

* Problems: 

You are limited to sending only 25 requests every 200 seconds to Steam, as Steam imposes restrictions on the number of requests within a short timeframe. To overcome this limitation, you can use a VPN or proxy server. For additional information, please refer to this link: https://medium.com/@DavidMBK/steam-trading-cards-information-21994b6572d0

## User Information

Within this section, you can review your level statistics, gaining insights into factors such as the typical speed of card packs drops and the associated probabilities. Additionally, you can compare different levels and obtain an "approximate price for leveling up at that level" (please note that this may vary due to the ever-changing market conditions).

Source of the formula for the cooldown : https://steamcommunity.com/groups/BadgesCollectors/discussions/0/630800444048297919/?ctp=10#c2686880925148364340

Other source: 
1. https://www.reddit.com/r/Steam/comments/10ctrjr/comment/j4i65m3/?utm_source=share&utm_medium=web2x&context=3

2. https://www.reddit.com/r/Steam/comments/bht6y1/comment/elwb6e4/?utm_source=share&utm_medium=web2x&context=3

3. https://steamcommunity.com/sharedfiles/filedetails/?id=145245037


![](https://i.imgur.com/syUl1qr.png)

Additional evidence, based on my experience (I leveled up during this period, so the cooldown time might be slightly adjusted):

![](https://i.imgur.com/yL0QQfY.png)
![](https://i.imgur.com/xhsXOsB.png)
![](https://i.imgur.com/Nu4ZNRB.png)
![](https://i.imgur.com/GwVf8TY.png)

With the range of 600 - 2000 games  (Yes, I am still receiving card sets)

## Exemplary Final Product

![](https://i.imgur.com/2PNlAOe.png)
![](https://i.imgur.com/wpgktm4.png)
![](https://i.imgur.com/pa0oQXW.png)

## Installation - With Prompt

1. Clone this repository in a folder: `git clone https://github.com/DavidMBK/Steam-Trading-Cards.git` 
*  if the command doesn't work, install Git : https://git-scm.com/download/win; otherwise, simply download the folder as is.
2. Enter the project directory: `cd your-project-name`
3. Install dependencies: `pip install -r requirements.txt`

## Usage - With Prompt

1. Enter in the project directory and run the application: `python main.py`
2. Follow the on-screen instructions to collect data, find real-time prices, check links, and compare costs.

## System Requirements

- Python 3.11
- Other dependencies listed in `requirements.txt`

## Contributions

I welcome contributions from the community! If you want to contribute, follow these steps:

* Fork this repository
* Create a branch for your change: `git checkout -b your-branch-name`
* Make your changes and commit: `git commit -m "Description of your changes"`
* Push your changes: `git push origin your-branch-name`
* Submit a Pull Request

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code in accordance with the terms of the MIT License.

## Disclaimer

I am not liable for any direct, indirect, consequential, incidental, or special damages arising out of or in any way connected with the use/misuse or inability to use this software.
