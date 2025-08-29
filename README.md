# 💱 Currency Converter

A fast, efficient, and beautifully designed currency converter web application built with Python Flask. Features real-time exchange rates, intelligent caching, and a responsive design.

**Created by Umar J** ⚡

## 🌟 Features

- **⚡ Lightning Fast**: Intelligent caching system reduces API calls and improves performance
- **🌍 Global Coverage**: Support for 150+ currencies worldwide
- **📱 Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **🔄 Real-time Rates**: Live exchange rates updated hourly
- **💨 Efficient**: Optimized for minimal resource usage and fast load times
- **🎨 Beautiful UI**: Modern gradient design with smooth animations
- **🔄 Currency Swap**: Quick currency swap functionality
- **📊 Detailed Results**: Shows both converted amount and exchange rate

## 🚀 Live Demo

Deploy this application on Vercel in minutes!

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **API**: ExchangeRate-API for real-time rates
- **Deployment**: Vercel
- **Styling**: Custom CSS with gradients and animations

## 📁 Project Structure

```
currency-converter/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── vercel.json        # Vercel deployment configuration
├── README.md          # Project documentation
└── templates/
    └── index.html     # Frontend template
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd currency-converter
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create the templates folder**
   ```bash
   mkdir templates
   ```
   
5. **Save the HTML template as `templates/index.html`**

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Open your browser**
   ```
   http://localhost:5000
   ```

## 🚀 Deployment on Vercel

### Method 1: Vercel CLI (Recommended)

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel
   ```

### Method 2: GitHub Integration

1. Push your code to GitHub
2. Connect your GitHub repository to Vercel
3. Vercel will automatically deploy on each push

### Method 3: Direct Upload

1. Go to [vercel.com](https://vercel.com)
2. Click "New Project"
3. Upload your project folder
4. Vercel will handle the rest!

## 🔧 Configuration

### Environment Variables (Optional)

You can add these environment variables in Vercel dashboard for enhanced functionality:

- `FLASK_ENV`: Set to `production` for deployment
- `API_KEY`: If you upgrade to a paid API plan

### API Rate Limits

- Free tier: 1,500 requests/month
- Cached responses reduce API usage
- Cache duration: 1 hour per currency pair

## 📚 API Documentation

### Endpoints

#### `GET /`
Returns the main currency converter interface.

#### `POST /api/convert`
Converts currency amounts.

**Request Body:**
```json
{
    "amount": 100,
    "from_currency": "USD",
    "to_currency": "EUR"
}
```

**Response:**
```json
{
    "result": 85.32,
    "from_currency": "USD",
    "to_currency": "EUR",
    "amount": 100
}
```

#### `GET /api/rates/{currency}`
Get all exchange rates for a base currency.

**Example:**
```
GET /api/rates/USD
```

## 🎯 Performance Optimizations

1. **Intelligent Caching**: Exchange rates are cached for 1 hour to reduce API calls
2. **Async Operations**: Non-blocking API requests
3. **Minimal Dependencies**: Lightweight Flask application
4. **CDN Ready**: Static assets optimized for CDN delivery
5. **Responsive Design**: Efficient CSS without external frameworks

## 🔐 Security Features

- Input validation and sanitization
- Rate limiting through API provider
- Error handling for network issues
- XSS protection through proper templating

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Troubleshooting

### Common Issues

1. **API Rate Limit Exceeded**
   - Wait for rate limit reset
   - Consider upgrading API plan
   - Increase cache duration

2. **Deployment Issues on Vercel**
   - Ensure `vercel.json` is in root directory
   - Check Python version compatibility
   - Verify all dependencies are in `requirements.txt`

3. **Currency Not Found**
   - Check currency code spelling
   - Ensure currency is supported by the API

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- ExchangeRate-API for providing reliable exchange rate data
- Vercel for seamless deployment platform
- Flask community for the excellent web framework

## 📞 Support

For support, issues, or feature requests, please create an issue in the repository.

---

**Built with ❤️ by Umar J**

### 🔗 Quick Links
- [Live Demo](#) (Replace with your Vercel URL)
- [API Documentation](#-api-documentation)
- [Deployment Guide](#-deployment-on-vercel)
- [Contributing](#-contributing)