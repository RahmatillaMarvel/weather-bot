# import the module
import python_weather
import asyncio
import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def get_weather_info(city):
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        # fetch a weather forecast from a city
        weather = await client.get(city)

        # get the current day's forecast temperature
        current_temperature = weather.current.temperature

        # create a string to store the weather information
        weather_info = f"🌡 Current Temperature in {city}: {current_temperature}°C\n\n"

        # get the weather forecast for a few days
        for forecast in weather.forecasts:
            date = forecast.date
            temperature = forecast.temperature

            # create a string for each day's forecast
            day_info = f"📅 {date}: {temperature}°C\n"

            # hourly forecasts
            for hourly in forecast.hourly:
                hour_info = f"  ⏰ {hourly.time}, 🌡 {hourly.temperature}°C, 📝 {hourly.description}\n"
                day_info += hour_info

            weather_info += day_info + "\n\n"

    return weather_info

cities = [
    # USA cities
    "New York",
    "Los Angeles",
    "Chicago",
    "San Francisco",
    "Miami",
    "Washington, D.C.",
    "Las Vegas",
    "Seattle",
    "Boston",
    "Atlanta",
    "Houston",
    "Dallas",
    "Denver",
    "Philadelphia",
    "Phoenix",
    "Austin",
    "San Diego",
    "Orlando",
    "New Orleans",
    "Detroit",
    
    # Russian cities
    "Moscow",
    "Saint Petersburg",
    "Novosibirsk",
    "Yekaterinburg",
    "Kazan",
    "Sochi",
    "Vladivostok",
    "Kaliningrad",
    "Nizhny Novgorod",
    "Samara",
    "Rostov-on-Don",
    "Krasnoyarsk",
    "Omsk",
    "Ufa",
    "Volgograd",
    "Perm",
    "Irkutsk",
    "Yaroslavl",
    "Tomsk",
    
    # Asia cities
    "Tokyo",
    "Beijing",
    "Seoul",
    "Bangkok",
    "Mumbai",
    "Tashkent",
    "Shanghai",
    "Delhi",
    "Istanbul",
    "Dubai",
    "Singapore",
    "Kuala Lumpur",
    "Jakarta",
    "Manila",
    "Hanoi",
    "Osaka",
    "Taipei",
    "Hong Kong",
    "Seoul",
    "Sydney",
    
    # Canada cities
    "Toronto",
    "Vancouver",
    "Montreal",
    "Calgary",
    "Ottawa",
    "Edmonton",
    "Quebec City",
    "Winnipeg",
    "Halifax",
    "Victoria",
    "Regina",
    "Hamilton",
    "Saskatoon",
    "London (Ontario)",
    "St. John's",
    "Windsor",
    "Kelowna",
    "Thunder Bay",
    "Charlottetown",
    "Whitehorse",
    
    # Africa cities
    "Cairo",
    "Nairobi",
    "Cape Town",
    "Lagos",
    "Casablanca",
    "Johannesburg",
    "Accra",
    "Marrakech",
    "Addis Ababa",
    "Dakar",
    "Nairobi",
    "Abuja",
    "Kigali",
    "Dar es Salaam",
    "Khartoum",
    "Luanda",
    "Tripoli",
    "Bamako",
    "Antananarivo",
    "Windhoek",
    
    # Europe cities
    "Paris",
    "London",
    "Berlin",
    "Rome",
    "Barcelona",
    "Amsterdam",
    "Vienna",
    "Prague",
    "Dublin",
    "Zurich",
    "Stockholm",
    "Warsaw",
    "Budapest",
    "Brussels",
    "Athens",
    "Copenhagen",
    "Helsinki",
    "Lisbon",
    # "Oslo",
    "Reykjavik"
]

# Create a keyboard with buttons for each city
menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.add(*[KeyboardButton(city) for city in cities])


API_TOKEN = 'Your API' #Change it to your API Token
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi! I'm Weather Bot. I can show you the current temperature in a city. Select a city from the menu below:", reply_markup=menu_keyboard)

@dp.message_handler(lambda message: message.text in cities, content_types=types.ContentTypes.TEXT)
async def send_weather(message: types.Message):
    city = message.text
    weather_info = await get_weather_info(city)

    # Split the weather information into separate messages for each day
    weather_messages = weather_info.split("\n\n\n")

    for weather_message in weather_messages:
        # Check if the weather message is not empty before sending
        if weather_message.strip():  # This checks if the message is not just whitespace
            await message.answer(weather_message)


if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # Start the bot
    executor.start_polling(dp, skip_updates=True)
