cities = ['topeka,kansas', 
          'kansas city,kansas', 
          'lawrence,kansas',
          'london',
          "paris",
          'bahstan',
          "tokyo",
          "dallas",
          "Chicago",
          "New York"
         ]
temps = []
lats = []
for city in cities:
    # Build query URL and request your results in Celsius
    query_url = f"{url}appid={api_key}&q={city}&units={units}"
    # Get weather data
    weather_response = requests.get(query_url)
    weather_json = weather_response.json()
    try:
        temperature = weather_json["main"]["temp"]
        lats.append(weather_json["coord"]["lat"])
        temps.append(temperature)
        print(f"The temperature in {city} is {temperature}")
    except:
        lats.append(0)
        temps.append(0)
        print(f"{city} is not found")
weather_dict = { 
    "city": cities,
    "temp": temps,
    "latitude": lats}
weather_df = pd.DataFrame(weather_dict)
plt.scatter(weather_df["latitude"], weather_df["temp"], marker='o')
plt.title("temperatures around the world")
plt.ylabel("temperature")
plt.xlabel("latitude")
plt.grid(True)