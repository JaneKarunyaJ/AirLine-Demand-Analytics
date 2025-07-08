# ✈️ Airline Demand Analytics Dashboard

A responsive Flask web app that fetches and visualizes airline booking trends using real-time or simulated flight data.  
Built to help travel businesses make smarter, data-driven decisions.

---

## ✨ Features

- 🔄 **Real-Time Flight Data** via OpenSky API
- 📊 **Interactive Charts** using Plotly:
  - Route Popularity
  - Price Trends
- 📈 **Smart Insights**:
  - Peak Demand Periods
  - Top Performing Routes
  - Dynamic Filtering by Route
- 📱 **Responsive Design** – works on desktop, tablet, and mobile

---

## 🚀 Quick Start

### ✅ Prerequisites
- Python 3.8 or higher
- `pip` package manager

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/JaneKarunyaJ/AirLine-Demand-Analytics.git
cd AirLine-Demand-Analytics
```

---

### 2️⃣ Create a virtual environment

```bash
python3 -m venv venv
```

---

### 3️⃣ Activate the environment

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

---

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### ▶️ Run the application

```bash
python main.py
```

Then open your browser and visit:  
👉 [http://localhost:5000](http://localhost:5000)

---

## 📡 Data Sources

### 🔌 Live API (Optional)

Uses OpenSky Network API for real-time flight data ✈️  
You can also integrate premium APIs like AviationStack.

Example usage:

```python
API_KEY = "your_api_key_here"
```

---

### 🧪 Simulated Sample Data

Preloaded with random demand and price simulation for testing.  
Example flights include:

- ✈️ Singapore Airlines SQ221 (SYD-SIN)
- 🦘 Qantas QF81 (SYD-SIN)
- 🐯 Scoot TR7 (SYD-SIN)

---

## 🧾 Project Structure

```bash
AirLine-Demand-Analytics/
├── main.py               # 🚀 Main Flask application logic
├── templates/
│   └── dashboard.html    # 🎨 Jinja2 HTML template
├── static/               # 🎯 Optional CSS/JS assets
├── requirements.txt      # 📦 Python dependencies
└── README.md             # 📘 This file
```

---

## 🛠️ Sample Custom Data Structure

You can extend the app with structured flight data like below:

```python
{
  "datetime": "2025-07-07 09:00",
  "airline": "Your Airline",
  "flight_number": "YA123",
  "route": "MEL-SYD",
  "price": 245.00,
  "status": "On Time"
}
```

---

## 🚀 Future Enhancements

- 🧠 ChatGPT integration for natural-language trend summaries
- 📁 CSV export of route and pricing insights
- 🗃 Persistent storage with SQLite or PostgreSQL
- 📆 Date-based and seasonal demand filtering
- 🔐 User login for data upload and access

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👩‍💻 Developed by

**Jane Karunya J**  
✨ [GitHub](https://github.com/JaneKarunyaJ)
