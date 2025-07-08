from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
import requests
from datetime import datetime
import numpy as np
from functools import lru_cache

app = Flask(__name__)

# Configuration
API_KEY = "your_aviationstack_key"  # Register at aviationstack.com
BASE_URL = "http://api.aviationstack.com/v1"

@lru_cache(maxsize=1, typed=False)
def fetch_flight_data():
    """Fetch real flight data from API with fallback to simulated data"""
    try:
        url = f"{BASE_URL}/flights?access_key={API_KEY}"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        flights = []
        for flight in data.get('data', [])[:50]:  # Limit to 50 flights
            # Safely extract all fields with fallbacks
            departure = flight.get('departure', {})
            arrival = flight.get('arrival', {})
            airline = flight.get('airline', {})
            flight_info = flight.get('flight', {})
            
            flights.append({
                'datetime': departure.get('scheduled', ''),
                'route': f"{departure.get('iata', '')}-{arrival.get('iata', '')}",
                'price': flight.get('price', 0),
                'airline': airline.get('name', 'Unknown'),
                'flight_number': flight_info.get('iata', ''),
                'status': flight.get('flight_status', 'Unknown')
            })
        
        df = pd.DataFrame(flights)
        # Ensure we have required columns
        if 'route' not in df.columns:
            df['route'] = 'Unknown-Unknown'
        return df
        
    except Exception as e:
        print(f"API Error: {e}, using simulated data")
        return generate_simulated_data()

def generate_simulated_data():
    """Generate realistic flight data when API fails"""
    now = datetime.now()
    routes = ["SYD-MEL", "MEL-BNE", "BNE-PER", "PER-ADL", "ADL-CBR"]
    airlines = ["Qantas", "Virgin Australia", "Jetstar", "Rex", "Air New Zealand"]
    
    data = []
    for _ in range(50):
        route = np.random.choice(routes)
        hour = np.random.randint(0, 24)
        dt = now.replace(hour=hour, minute=0, second=0, microsecond=0)
        
        data.append({
            'datetime': dt,
            'route': route,
            'price': 150 + len(route)*10 * (0.8 + 0.4*np.random.random()),
            'airline': np.random.choice(airlines),
            'flight_number': f"{np.random.choice(['QA','VA','JQ','RX','NZ'])}{np.random.randint(100,999)}",
            'status': np.random.choice(["On Time", "Delayed", "Cancelled"])
        })
    
    return pd.DataFrame(data)

def generate_insights(df):
    """Generate actionable insights from flight data"""
    insights = {}
    
    try:
        # Peak demand hours
        if 'datetime' in df.columns:
            df['hour'] = pd.to_datetime(df['datetime']).dt.hour
            peak_hours = df['hour'].value_counts().idxmax()
            insights['peak_hours'] = f"{peak_hours}:00-{peak_hours+1}:00"
        else:
            insights['peak_hours'] = "No time data"
        
        # Best deals (lowest price routes)
        if 'route' in df.columns and 'price' in df.columns:
            best_deals = df.groupby('route')['price'].mean().nsmallest(3)
            insights['best_deals'] = ", ".join([f"{route} (${int(price)}" 
                                              for route, price in best_deals.items()])
        else:
            insights['best_deals'] = "No route/price data"
        
        # Top airlines
        if 'airline' in df.columns:
            top_airlines = df['airline'].value_counts().head(3)
            insights['top_airlines'] = ", ".join([f"{airline} ({count} flights)" 
                                                for airline, count in top_airlines.items()])
        else:
            insights['top_airlines'] = "No airline data"
    
    except Exception as e:
        print(f"Insight generation error: {e}")
        insights = {
            'peak_hours': 'Data unavailable',
            'best_deals': 'Data unavailable',
            'top_airlines': 'Data unavailable'
        }
    
    return insights

@app.route("/", methods=["GET", "POST"])
def dashboard():
    # Initialize with empty defaults
    default_response = {
        'charts': {},
        'insights': {
            'peak_hours': 'No data',
            'best_deals': 'No data',
            'top_airlines': 'No data'
        },
        'flights': [],
        'routes': [],
        'airlines': [],
        'current_filters': {
            'route': '',
            'min_price': '',
            'max_price': '',
            'airline': ''
        },
        'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    try:
        df = fetch_flight_data()
        
        # Initialize filters
        current_filters = {
            'route': request.form.get('route', ''),
            'min_price': request.form.get('min_price', ''),
            'max_price': request.form.get('max_price', ''),
            'airline': request.form.get('airline', '')
        }
        
        # Apply filters if columns exist
        if 'route' in df.columns and current_filters['route']:
            df = df[df['route'] == current_filters['route']]
        if 'price' in df.columns:
            if current_filters['min_price']:
                try:
                    df = df[df['price'] >= float(current_filters['min_price'])]
                except ValueError:
                    pass
            if current_filters['max_price']:
                try:
                    df = df[df['price'] <= float(current_filters['max_price'])]
                except ValueError:
                    pass
        if 'airline' in df.columns and current_filters['airline']:
            df = df[df['airline'] == current_filters['airline']]
        
        # Generate charts only if we have data
        charts = {}
        if not df.empty:
            # Top Routes Chart
            if 'route' in df.columns:
                route_counts = df['route'].value_counts().head(5).reset_index()
                route_counts.columns = ['route', 'count']
                charts['routes'] = px.bar(
                    route_counts,
                    x='route',
                    y='count',
                    title="Top 5 Busiest Routes"
                ).to_html(full_html=False)
            
            # Price Trends Chart
            if 'datetime' in df.columns and 'price' in df.columns:
                price_trend = df.groupby(pd.Grouper(key='datetime', freq='6H'))['price'].mean().reset_index()
                charts['prices'] = px.line(
                    price_trend,
                    x='datetime',
                    y='price',
                    title="Price Trends (6hr intervals)"
                ).to_html(full_html=False)
            
            # Airline Market Share
            if 'airline' in df.columns:
                airline_counts = df['airline'].value_counts().reset_index()
                airline_counts.columns = ['airline', 'count']
                charts['airlines'] = px.pie(
                    airline_counts,
                    values='count',
                    names='airline',
                    title="Airline Market Share"
                ).to_html(full_html=False)
        
        # Generate insights
        insights = generate_insights(df)
        
        # Prepare flight data for table
        flight_data = []
        if not df.empty:
            columns_to_show = ['datetime', 'airline', 'flight_number', 'route', 'price', 'status']
            available_columns = [col for col in columns_to_show if col in df.columns]
            
            if available_columns:
                flight_data = df[available_columns]
                if 'datetime' in flight_data.columns:
                    flight_data['datetime'] = pd.to_datetime(flight_data['datetime']).dt.strftime('%Y-%m-%d %H:%M')
                flight_data = flight_data.to_dict('records')
        
        return render_template(
            "dashboard.html",
            charts=charts,
            insights=insights,
            flights=flight_data,
            routes=sorted(df['route'].unique()) if 'route' in df.columns else [],
            airlines=sorted(df['airline'].unique()) if 'airline' in df.columns else [],
            current_filters=current_filters,
            last_updated=datetime.now().strftime("%Y-%m-%d %H:%M")
        )
    
    except Exception as e:
        print(f"Dashboard error: {e}")
        return render_template("dashboard.html", **default_response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)