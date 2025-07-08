# ✈️📊 Airline Demand Analytics Dashboard

A Python Flask web application that visualizes airline booking trends using real-time flight data and simulated insights.  
Designed for businesses in the **travel and hospitality** industry to make smarter decisions based on booking demand patterns.

---

## 🔍 Overview

This dashboard fetches flight data via the **OpenSky Network API**, simulates pricing and demand, and presents insights like:
- Most popular flight routes
- Pricing trends over time
- High-demand routes and periods

Built with:
- 🐍 Python (Flask, Pandas)
- 📊 Plotly for interactive charts
- 🌐 HTML & Jinja for web rendering

---

## 📦 Dataset / Data Source

The application **does not require a local dataset**. It pulls real-time public flight data using:

| Source | Purpose |
|--------|---------|
| [OpenSky Network API](https://opensky-network.org/) | Real-time aircraft location and route data |

Simulated attributes:
- **Price** is randomly generated based on route hash
- **Demand** is a simulated score based on callsign hash

---

## 🧠 Features

| Feature | Description |
|--------|-------------|
| ✈ Real-Time API Integration | Live aircraft data from OpenSky API |
| 📈 Route Popularity Analysis | Top 5 routes shown using bar charts |
| 💹 Price Trend Analysis | Interactive line chart of average price per day |
| 🔎 Filter by Route | Dropdown selector for route-based insights |
| 📱 Responsive UI | Works on all screen sizes (mobile/tablet/desktop) |

---

## ⚙️ Installation & Usage

### ✅ Prerequisites
- Python 3.8+
- pip

### 🚀 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/airline-demand-analytics.git
cd airline-demand-analytics

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python main.py
Then open your browser at: http://127.0.0.1:5000

🧾 Project Structure
php
Copy
Edit
airline-demand-analytics/
├── main.py               # Core Flask backend with chart logic
├── requirements.txt      # Python dependencies
├── templates/
│   └── dashboard.html    # Jinja2-based web UI template
├── static/               # (Optional) CSS or JS files
└── README.md             # Project documentation
