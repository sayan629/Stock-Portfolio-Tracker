# Stock Portfolio Tracker
import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity
        print(f"Added {quantity} shares of {symbol}.")

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if self.portfolio[symbol] > quantity:
                self.portfolio[symbol] -= quantity
                print(f"Removed {quantity} shares of {symbol}.")
            else:
                del self.portfolio[symbol]
                print(f"Removed all shares of {symbol}.")
        else:
            print("Stock not found in portfolio.")

    def view_portfolio(self):
        if not self.portfolio:
            print("Your portfolio is empty.")
            return

        print("\nYour Stock Portfolio:")
        for symbol, quantity in self.portfolio.items():
            stock = yf.Ticker(symbol)
            current_price = stock.history(period='1d')['Close'].iloc[-1]
            total_value = quantity * current_price
            print(f"{symbol}: {quantity} shares @ ${current_price:.2f} each | Total Value: ${total_value:.2f}")

if __name__ == "__main__":
    portfolio = StockPortfolio()
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            symbol = input("Enter stock symbol (e.g., AAPL, TSLA): ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)
        elif choice == "2":
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity to remove: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == "3":
            portfolio.view_portfolio()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please try again.")

