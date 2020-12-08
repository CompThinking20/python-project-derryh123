

##def weather():
    ##This function focuses on providing weather
    ##updates. I would need to provide a source first

##  resp = requests.get('')

  ##esponse.json() returns a JSON object. The requests are generally used to fetch the content from a particular resource URI.

 ## weatherData = resp.json()
  ##return weatherData



from tkinter import * from tkinter import messagebox

def tell_weather() :

    import requests, json

    api_key = "Your_API_key"


    base_url = "http://api.openweathermap.org/data/2.5/weather?"


    city_name = city_field.get()

    complete_url = base_url + "appid =" + api_key
                             + "&q =" + city_name

    response = requests.get(complete_url)

    x = response.json()
