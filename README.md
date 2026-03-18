# 🌤️ AI Weather Assistant

An AI-powered weather assistant that fetches real-time weather data for any city and generates a friendly, human-readable summary using an LLM.

---

## 🚀 How It Works

1. You enter a city name
2. The app fetches the city's coordinates using the **Open-Meteo Geocoding API**
3. It then retrieves live weather data (temperature, wind speed, humidity) using the **Open-Meteo Weather API**
4. The data is sent to **Groq's LLaMA 3.3 70B** model, which generates a natural, friendly weather summary
5. The summary is printed in your terminal

---

## 🛠️ Tech Stack

- **Python**
- **Open-Meteo API** – Geocoding + Weather data (free, no key needed)
- **Groq API** – LLM inference (LLaMA 3.3 70B)

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-weather-assistant.git
cd ai-weather-assistant
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory (use `.env.example` as a reference):

```bash
cp .env.example .env
```

Then open `.env` and add your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

> You can get a free Groq API key at [https://console.groq.com](https://console.groq.com)

---

## ▶️ Run the App

```bash
python main.py
```

You'll be prompted to enter a city name:

```
Enter a city name: London

Weather Summary for London:
It's a cool and breezy day in London at 14°C, with winds picking up at 
20 km/h and humidity sitting at 72%. You might want to grab a light jacket 
if you're heading out!
```

---

## 📁 Project Structure

```
ai-weather-assistant/
│
├── main.py            # Main application file
├── requirements.txt   # Python dependencies
├── .env.example       # Environment variable template
├── .gitignore         # Git ignored files
└── README.md          # Project documentation
```

---

## 🔑 Environment Variables

| Variable       | Description                        |
|----------------|------------------------------------|
| `GROQ_API_KEY` | Your API key from console.groq.com |

---

## 📦 Dependencies

- `requests` – HTTP calls to external APIs
- `python-dotenv` – Loading environment variables from `.env`

---

## 👨‍💻 Author

Built by a beginner exploring the world of AI agents. 🚀