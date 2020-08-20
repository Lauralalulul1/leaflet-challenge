temps = []
for city in cities:
    # Build query URL and request your results in Celsius
    query_url = f"{url}appid={api_key}&q={city}&units={units}"
    # Get weather data
    weather_response = requests.get(query_url)
    weather_json = weather_response.json()
    temperature = weather_json["main"]["temp"]
    temps.append(temperature)
    print(f"The temperature in {city} is {temperature}")