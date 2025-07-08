# ✈️ Airline Demand Analytics Dashboard

A responsive Flask web app that fetches and visualizes airline booking trends using real-time or simulated flight data. Built to help travel businesses make smarter, data-driven decisions.

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
- Python 3.8 or above
- `pip` package manager

### ⚙️ Installation

```bash
# 1. Clone the repository
git clone hhttps://github.com/JaneKarunyaJ/AirLine-Demand-Analytics.git
cd AirLine-Demand-Analytics

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
▶️ Run the Application
bash
Copy
Edit
python main.py
Then open your browser and go to:
👉 http://localhost:5000

📡 Data Sources
Live API (Optional):
You can integrate APIs like AviationStack or OpenSky.

Sample API integration (replace with your key):

python
Copy
Edit
API_KEY = "your_api_key_here"
Simulated Sample Data:
Preloaded with random demand and price simulation for testing.

Sample flights include:

Singapore Airlines SQ221 (SYD-SIN)

Qantas QF81 (SYD-SIN)

Scoot TR7 (SYD-SIN)

🧾 Project Structure
php
Copy
Edit
airline-analytics/
├── main.py               # Main Flask application logic
├── templates/
│   └── dashboard.html    # Jinja2 HTML template
├── static/               # (Optional) CSS/JS assets
├── requirements.txt      # Python dependencies
└── README.md             # This file

python
Copy
Edit
{
  "datetime": "2025-07-07 09:00",
  "airline": "Your Airline",
  "flight_number": "YA123",
  "route": "MEL-SYD",
  "price": 245.00,
  "status": "On Time"
}
