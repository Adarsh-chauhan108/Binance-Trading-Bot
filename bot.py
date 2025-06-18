from binance.client import Client
import logging
#
class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        
        if testnet:
            self.client = Client(api_key, api_secret, testnet=True)
        else:
            self.client = Client(api_key, api_secret)

        print("✅ Bot initialized with Binance Futures Testnet")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            if order_type == 'MARKET':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='MARKET',
                    quantity=quantity
                )
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type='LIMIT',
                    timeInForce='GTC',
                    quantity=quantity,
                    price=price
                )
            else:
                print("❌ Unsupported order type")
                return None

            print("✅ Order placed:", order['orderId'])
            logging.info(f"Order placed: {order}")
            return order

        except Exception as e:
            print("❌ Order failed:", e)
            logging.error(f"Error placing order: {e}")
            return None
