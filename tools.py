import requests
import qrcode
from datetime import datetime

# 1. أداة الوقت
def get_current_time():
    """Returns the current time as a string."""
    return datetime.now().strftime("%H:%M:%S")

# 2. أداة الطقس (معتمدة على API)
def get_weather(location: str):
    """Gets the current weather for a specific location using Open-Meteo API."""
    # للتسهيل هنستخدم إحداثيات ثابتة لدبي كمثال، أو ممكن تطورها وتخليها تاخد Lat/Lon
    # Dubai Coordinates
    lat, lon = 25.2048, 55.2708 
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
    
    try:
        response = requests.get(url).json()
        temp = response['current']['temperature_2m']
        return f"The temperature in Dubai is {temp}°C"
    except Exception as e:
        return f"Error fetching weather: {str(e)}"

# 3. أداة كتابة الملفات
def write_file(filename: str, content: str):
    """Writes content to a text file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Successfully wrote to {filename}"
    except Exception as e:
        return f"Error writing file: {str(e)}"