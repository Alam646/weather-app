# import the module
import python_weather
import asyncio
import os

async def getweather():
    # declare the client. the measuring unit used defaults to the metric system (Celsius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        # fetch a weather forecast from a city
        weather = await client.get('New York')

        # returns the current day's forecast temperature (int)
        print(f"Current temperature in New York: {weather.temperature}°F")

        # get the weather forecast for a few days
        for daily in weather.daily:
            print(f"Date: {daily.date}")
            print(f"  High: {daily.highest_temperature}°F")
            print(f"  Low: {daily.lowest_temperature}°F")
            print(f"  Sunrise: {daily.sunrise}")
            print(f"  Sunset: {daily.sunset}")
            print(f"  Moon Phase: {daily.moon_phase}")

            # hourly forecasts
            for hourly in daily.hourly_forecasts:
                print(f'    Time: {hourly.time}, Temperature: {hourly.temperature}°F, Condition: {hourly.condition}')

if __name__ == '__main__':
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop for more details
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())
