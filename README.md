# Tkinter-weather-GUI
A Python GUI to show the weather of a place using Tkinter and a weather API

The [weatherstack](https://weatherstack.com/) API is called to get live weather details each time the program is executed. The date, time, temperature, humidity, UV index, etc change based on the current scenario.

To get the weather of a place, create an account on weatherstack and generate your access key. After executing the code, you will be required to enter the name of a city in the console, which will call the API and get the current weather details of the city.

The color of the UV index label is based on the UV index. As the value gets higher from 0 to 11+, the color will change from green, to yellow, orange, red and finally dark violet.

The [weatherJSON.py](https://github.com/NiladriMallik/tkinter-weather-GUI/blob/main/weatherJSON.py) file contains a sample result for reference.

Below is the screenshot of the GUI executed at a particular time:
![screenshot](https://user-images.githubusercontent.com/51795733/189119761-daa81c13-311a-400e-9903-ed0d3a579c67.png)
