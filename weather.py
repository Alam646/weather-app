# Import the necessary modules
import python_weather
import asyncio
import os

async def getweather():
    # Declare the client with the imperial unit system
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        # Fetch a weather forecast for New York
        weather = await client.get('New York')

        # Print general weather information
        print(f"Location: {weather.location}")
        print(f"Temperature: {weather.temperature}°F")
        print(f"Feels like: {weather.feels_like}°F")
        print(f"Description: {weather.description}")
        
        # Print daily forecasts
        for daily in weather.daily_forecasts:
            print(f"Date: {daily.date}, High: {daily.highest_temperature}°F, Low: {daily.lowest_temperature}°F")
            for hourly in daily.hourly_forecasts:
                print(f" --> Hour: {hourly.time}, Temp: {hourly.temperature}°F, Description: {hourly.description}")

if __name__ == '__main__':
    # See https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())
