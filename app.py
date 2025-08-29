from flask import Flask, render_template, request, jsonify
import requests
import os
from datetime import datetime, timedelta
import json

app = Flask(__name__)

# Cache for storing exchange rates to improve efficiency
rate_cache = {}
cache_expiry = {}

class CurrencyConverter:
    def __init__(self):
        # Using exchangerate-api.com (free tier allows 1500 requests/month)
        self.base_url = "https://api.exchangerate-api.com/v4/latest/"
        
    def get_exchange_rate(self, from_currency, to_currency):
        """Get exchange rate with caching for efficiency"""
        cache_key = f"{from_currency}_{to_currency}"
        
        # Check if we have cached data and it's not expired
        if (cache_key in rate_cache and 
            cache_key in cache_expiry and 
            datetime.now() < cache_expiry[cache_key]):
            return rate_cache[cache_key]
        
        try:
            # Fetch fresh data
            response = requests.get(f"{self.base_url}{from_currency}", timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if to_currency in data['rates']:
                rate = data['rates'][to_currency]
                
                # Cache the rate for 1 hour
                rate_cache[cache_key] = rate
                cache_expiry[cache_key] = datetime.now() + timedelta(hours=1)
                
                return rate
            else:
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rate: {e}")
            return None
    
    def convert_currency(self, amount, from_currency, to_currency):
        """Convert currency amount"""
        if from_currency == to_currency:
            return amount
            
        rate = self.get_exchange_rate(from_currency, to_currency)
        if rate is None:
            return None
            
        return round(amount * rate, 2)
    
    def get_supported_currencies(self):
        """Get list of supported currencies"""
        try:
            response = requests.get(f"{self.base_url}USD", timeout=10)
            response.raise_for_status()
            data = response.json()
            return list(data['rates'].keys()) + ['USD']
        except:
            # Fallback list of major currencies
            return ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD']

converter = CurrencyConverter()

@app.route('/')
def index():
    """Main page"""
    currencies = converter.get_supported_currencies()
    return render_template('index.html', currencies=sorted(currencies))

@app.route('/api/convert', methods=['POST'])
def convert_api():
    """API endpoint for currency conversion"""
    try:
        data = request.get_json()
        amount = float(data['amount'])
        from_currency = data['from_currency'].upper()
        to_currency = data['to_currency'].upper()
        
        result = converter.convert_currency(amount, from_currency, to_currency)
        
        if result is None:
            return jsonify({'error': 'Conversion failed'}), 400
            
        return jsonify({
            'result': result,
            'from_currency': from_currency,
            'to_currency': to_currency,
            'amount': amount
        })
        
    except (ValueError, KeyError) as e:
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/api/rates/<currency>')
def get_rates(currency):
    """Get all exchange rates for a base currency"""
    try:
        response = requests.get(f"{converter.base_url}{currency.upper()}", timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except:
        return jsonify({'error': 'Failed to fetch rates'}), 400

# Vercel deployment handler
if __name__ == '__main__':
    app.run(debug=True)