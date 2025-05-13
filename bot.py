import time
import requests

# KyaTeN Trading Bot - Simple Test Version

def check_market():
    print("Checking market price...")
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    if response.status_code == 200:
        data = response.json()
        price = data['bpi']['USD']['rate']
        print(f"Current BTC Price: ${price}")
    else:
        print("Failed to get price.")

def place_trade():
    print("Placing trade (just simulating)...")
    print("Trade done!")

def main():
    while True:
        check_market()
        place_trade()
        print("Waiting 1 minute...\n")
        time.sleep(60)

if __name__ == "__main__":
    main()
