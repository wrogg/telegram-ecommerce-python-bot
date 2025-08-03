# Configuration file for Telegram Cryptocurrency Shop Bot
# Copy this file to config.py and update with your actual values

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # Get from @BotFather
OXAPAY_API_KEY = ""  # Leave empty for testing without crypto payment provider

# Admin Configuration
ADMIN_USER_ID = 123456789  # Replace with your Telegram user ID

# Bot Settings
SUPPORT_HANDLE = "@your_support_handle"
SHOP_IMAGE = "shop_banner.jpg"  # Placeholder image filename
CURRENCY = "GBP"

# Product Configuration
# Update these with your actual products
PRODUCTS = [
    {
        "id": 1,
        "name": "Sample Product A",
        "description": "Description for Sample Product A.",
        "prices": {1: 10.0, 5: 45.0, 10: 80.0},  # Quantity: Price
        "image": "product_a.jpg"
    },
    {
        "id": 2,
        "name": "Sample Product B", 
        "description": "Description for Sample Product B.",
        "prices": {1: 20.0, 5: 90.0, 10: 160.0},
        "image": "product_b.jpg"
    }
]

# Database Configuration
DATABASE_FILE = "orders.db"

# Security Settings
MAX_ORDERS_PER_USER = 10  # Maximum orders per user per day
RATE_LIMIT_SECONDS = 60   # Rate limiting for admin commands 