# ChatGPT_FunctonCalling Example

**Title: Function Calling with OpenWeather API and ChatGPT 3.5 Turbo**

**Description:**

This repository contains a simple application showcasing the "Function Calling" feature of ChatGPT, which was announced last month (June 13, 2023) [here](https://openai.com/blog/function-calling-and-other-api-updates).

**Application Overview:**

The implemented application demonstrates how to utilize the "Function Calling" capability to enable ChatGPT 3.5 Turbo to respond to complex questions that it wouldn't be able to handle alone. Specifically, the application combines the power of the OpenWeather API and ChatGPT 3.5 Turbo to retrieve weather information for a specified location based on the provided location data and country code.

**How it Works:**

The application takes user input containing location information (such as city name and country code) and feeds it into the "Function Calling" API. ChatGPT 3.5 Turbo converts this data into a format that the OpenWeather API can use and OpenWeather funciton fetches the desired weather information for the specified region. The retrieved data is then presented to the user with the help of gpt in response to the user's original question.
