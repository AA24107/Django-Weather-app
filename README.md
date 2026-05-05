# Weather Detector (Django)

A simple Django-based web application that fetches real-time weather data using the OpenWeather API and displays it based on user input.

---

## Features

* Search the weather by city name
* Fetch real-time data from OpenWeather API
* Display:

  * Temperature (°C)
  * Pressure
  * Coordinates (Latitude & Longitude)
  * Country code
* Backend built with Django
* API integration using Python (`urllib`)

---

## Tech Stack

* Python
* Django
* HTML / CSS
* OpenWeather API

---

## How It Works

1. User enters a city name
2. Django view processes the request
3. API call is made to OpenWeather
4. JSON response is parsed
5. Data is displayed on the webpage

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/AA24107/Django-weather-app.git
cd weather-detector
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install django
```

### 4. Add your API key

In `views.py`, replace:

```python
appid=YOUR_API_KEY
```

Get your API key from: https://openweathermap.org/

---

### 5. Run the server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

## ⚠️ Known Limitations

* Basic UI (minimal styling)
* No error handling for invalid city inputs (can be improved)
* Uses `urllib` instead of modern libraries like `requests.`

---

## Future Improvements

* Better UI (Bootstrap / Tailwind)
* Add weather description (e.g., Clear, Rainy)
* Error handling for invalid input
* Switch to `requests` library
* Integrate with IoT sensors (e.g., DHT11) for local + API data

---

## Notes

This project was built as part of learning backend development and API integration.
It demonstrates how to connect a Django application with an external API and process real-world data.

---

## 📄 License

This project is open-source and available under the MIT License.
