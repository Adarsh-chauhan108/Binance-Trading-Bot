from bot import BasicBot
import logging

# Setup logging
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    print("Welcome to the Binance Futures Trading Bot")

    api_key = input("Enter your Binance API Key: ")
    api_secret = input("Enter your Binance API Secret: ")

    bot = BasicBot(api_key, api_secret)

    symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY or SELL): ").upper()
    order_type = input("Enter order type (MARKET or LIMIT): ").upper()
    quantity = float(input("Enter quantity: "))

    price = None
    if order_type == 'LIMIT':
        price = input("Enter price for LIMIT order: ")

    result = bot.place_order(symbol, side, order_type, quantity, price)
    print("Result:", result)

if __name__ == '__main__':
    main()
