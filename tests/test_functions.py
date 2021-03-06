import unittest
import json
import requests
from Functions import weather_choices, check_exists, custom_weather_choices
from Weather import json_convert, Weather

url: str = f"http://api.openweathermap.org/data/2.5/weather?q=melbourne,au&units=metric&appid=b2cf60917edb97ded95da68172607141"
response = requests.request("GET", url)
response_loaded = json.loads(response.text)
cur_temp = f"Current Temperature: {int(response_loaded['main']['temp'])} Degrees Celsius"
max_temp = f"Maximum Temperature: {int(response_loaded['main']['temp_max'])} Degrees Celsius"
min_temp = f"Minimum Temperature: {int(response_loaded['main']['temp_min'])} Degrees Celsius"
feels_like = f"Feels Like: {int(response_loaded['main']['feels_like'])} Degrees Celsius"
humidity = f"Humidity: {response_loaded['main']['humidity']}%"
test_weather = Weather('melbourne')


class testFunctions(unittest.TestCase):
    def test_weather_choices(self):
        result = weather_choices('1', 'melbourne')
        self.assertEqual(result, cur_temp, msg=f"Results: {result}, Expected: {cur_temp}")

        result = weather_choices('2', 'melbourne')
        self.assertEqual(result, max_temp, msg=f"Results: {result}, Expected: {max_temp}")

        result = weather_choices('3', 'melbourne')
        self.assertEqual(result, min_temp, msg=f"Results: {result}, Expected: {min_temp}")

        result = weather_choices('4', 'melbourne')
        self.assertEqual(result, feels_like, msg=f"Results: {result}, Expected: {feels_like}")

        result = weather_choices('5', 'melbourne')
        self.assertEqual(result, humidity, msg=f"Results: {result}, Expected: {humidity}")

    def test_check_exists(self):
        result = check_exists(test_weather)
        self.assertEqual(result, None, msg=f"Results: {result}, Expected: {None}")

    def test_custom_weather_choices(self):
        result = custom_weather_choices('1', test_weather)
        self.assertEqual(result, cur_temp, msg=f"Results: {result}, Expected: {cur_temp}")

        result = custom_weather_choices('2', test_weather)
        self.assertEqual(result, max_temp, msg=f"Results: {result}, Expected: {max_temp}")

        result = custom_weather_choices('3', test_weather)
        self.assertEqual(result, min_temp, msg=f"Results: {result}, Expected: {min_temp}")

        result = custom_weather_choices('4', test_weather)
        self.assertEqual(result, feels_like, msg=f"Results: {result}, Expected: {feels_like}")

        result = custom_weather_choices('5', test_weather)
        self.assertEqual(result, humidity, msg=f"Results: {result}, Expected: {humidity}")
