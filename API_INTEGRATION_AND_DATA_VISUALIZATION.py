import requests
import matplotlib.pyplot as plt
import seaborn as sns

API_Key ='028f0f55c89c2787ec1a9810d9cb1069'
cities =['Agra', 'Mumbai', 'Delhi', 'Chennai', 'Kolkata', 'Pune']

temperatures = []
feels_like = []
humidity = []


for city in cities:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and 'main' in data:
        temperatures.append(data['main']['temp'])
        feels_like.append(data['main']['feels_like'])
        humidity.append(data['main']['humidity'])
    else:
        print(f"Error fetching data for {city}: {data}")
        temperatures.append(0)
        feels_like.append(0)
        humidity.append(0)

# ---------------- Step 3: Create Visualizations ----------------

# Set Seaborn style
sns.set(style="whitegrid")

# ---- Temperature vs Cities ----
plt.figure(figsize=(10,5))
plt.bar(cities, temperatures, color='orange', label='Temperature (°C)')
plt.bar(cities, feels_like, color='#FF69B4', alpha=0.6, label='Feels Like (°C)')
plt.xlabel("Cities")
plt.ylabel("Temperature (°C)")
plt.title("Current Temperature and Feels Like Temperature in Cities")
plt.legend()
plt.show()

# ---- Humidity vs Cities ----
plt.figure(figsize=(10,5))
sns.barplot(x=cities, y=humidity, palette="coolwarm")
plt.xlabel("Cities")
plt.ylabel("Humidity (%)")
plt.title("Humidity in Different Cities")
plt.show()
