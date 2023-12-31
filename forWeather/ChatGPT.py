# import os
# from dotenv import load_dotenv
import openai
import json
import requests
import apiKeys

# load_dotenv()

# openai.api_key = os.getenv("OPENAI_API_KEY")
# API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

# Due to dotenv not working, APIs have been imported to the main file using import.py.
openai.api_key = apiKeys.OPENAI_API_KEY
API_KEY = apiKeys.OPENWEATHERMAP_API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
# city = "Istanbul"
# country_code = "TR"


def get_current_weather(city, country_code, unit="fahrenheit"):
    """Get the current weather in a given location"""
    params = {
        "q": f"{city},{country_code}",
        "appid": API_KEY,
        "units": "imperial" if unit == "fahrenheit" else "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()
    print("data of get_current_weather func: " +str(data) + "\n" + "\n")
    """ {'coord': {'lon': 28.9833, 'lat': 41.0351}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 26.29, 'feels_like': 26.29, 'temp_min': 25.68, 'temp_max': 30.09, 'pressure': 1011, 'humidity': 65}, 'visibility': 10000, 'wind': {'speed': 3.09, 'deg': 130}, 'clouds': {'all': 0}, 'dt': 1691045908, 'sys': {'type': 1, 'id': 6970, 'country': 'TR', 'sunrise': 1691031678, 'sunset': 1691083152}, 'timezone': 10800, 'id': 745042, 'name': 'Istanbul', 'cod': 200} """
    
    if data["cod"] == 200:
        weather_info = {
            "temperature": data["main"]["temp"],
            "unit": "fahrenheit" if unit == "fahrenheit" else "celsius",
            "description": data["weather"][0]["description"],
        }
        print("weather info::::" + str(weather_info) + "\n" + "\n" + "\n")
        return json.dumps(weather_info)
    else:
        print("Failed to fetch weather data.")
        return None


def run_conversation():
    # Step 1: send the conversation and available functions to GPT
    messages = [{"role": "user", "content": "What's the weather like in Athens?"}]
    functions = [
        {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city name, e.g. Istanbul",
                    },
                    "country_code": {
                        "type": "string",
                        "description": "The country code, e.g. TR",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["city", "country_code"],
            },
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        # function_call="auto",  # auto is default, but we'll be explicit
    )
    
    response_message = response["choices"][0]["message"] 
    # print(" response message of run_conversation func: " + str(response_message) + "\n" + "\n")


    # Step 2: check if GPT wanted to call a function
    if response_message.get("function_call"):
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "get_current_weather": get_current_weather,
        }  # only one function in this example, but you can have multiple
        
        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        
        function_response = fuction_to_call(
            city=function_args.get("city"),
            country_code=function_args.get("country_code"),
            unit=function_args.get("unit"),
        )
        
        # Step 4: send the info on the function call and function response to GPT
        print(messages)
        print("\n" + "\n" +"\n")
        messages.append(response_message)  # extend conversation with assistant's reply
        print(messages)
        print("\n" + "\n" +"\n")
        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        )  # extend conversation with function response
        print(messages)
        print("\n" + "\n" +"\n")
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        
        return second_response["choices"][0]["message"]["content"]  # Extract the content of the message
    else:
        return response_message["content"]


print("\n" + "\n" + "\n" + run_conversation())

