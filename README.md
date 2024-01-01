# Weather Bot
Weather Bot is a simple Telegram bot that provides current weather information for various cities around the world. Users can select a city from a predefined list, and the bot will respond with the current temperature and a forecast for the upcoming days.

## Features
* Get current temperature in a selected city.
* View a detailed weather forecast for the next few days, including hourly updates.
## How to Use
1. Start a chat with the Weather Bot on Telegram: Weather Bot.
2. Use the "/start" command to initiate the bot and receive a list of cities.
3. Select a city from the provided list to receive the current temperature and weather forecast.
## Available Commands
1. **/start**: Initiate the bot and receive a list of cities.
2. **City Names**: Select a city from the provided list to get weather information.
## Cities Supported
The bot supports weather information for cities in the USA, Russia, Asia, Canada, Africa, and Europe.
## Installation
To run the bot locally, follow these steps:
1. Clone this repository:
```bash
git clone https://github.com/RahmatillaMarvel/weather-bot.git
```
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
3. Set up your Telegram Bot API token:

* Obtain a token by creating a new bot on BotFather.
* Replace the placeholder token in the **main.py** file with your actual token.
4. Run the bot:
```bash
python main.py
```
## Contributing
If you have suggestions, enhancements, or bug fixes, feel free to open an issue or create a pull request.