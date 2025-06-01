from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict, Any


# Observer interface
class StockObserver(ABC):
    @abstractmethod
    def update(self, stock_symbol: str, price: float, change: float, timestamp: datetime):
        pass


# Subject interface
class StockSubject(ABC):
    @abstractmethod
    def attach(self, observer: StockObserver):
        pass

    @abstractmethod
    def detach(self, observer: StockObserver):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


# Concrete subject
class Stock(StockSubject):
    def __init__(self, symbol: str, initial_price: float):
        self.symbol = symbol
        self._price = initial_price
        self._previous_price = initial_price
        self._observers: List[StockObserver] = []
        self._timestamp = datetime.now()

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float):
        if new_price != self._price:
            self._previous_price = self._price
            self._price = new_price
            self._timestamp = datetime.now()
            self.notify_observers()

    def attach(self, observer: StockObserver):
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Observer attached to {self.symbol}")

    def detach(self, observer: StockObserver):
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Observer detached from {self.symbol}")

    def notify_observers(self):
        change = self._price - self._previous_price
        print(f"Notifying {len(self._observers)} observers about {self.symbol} price change")

        for observer in self._observers:
            observer.update(self.symbol, self._price, change, self._timestamp)


# Concrete observers
class StockPriceDisplay(StockObserver):
    def __init__(self, name: str):
        self.name = name
        self.watched_stocks: Dict[str, Dict[str, Any]] = {}

    def update(
        self, stock_symbol: str, price: float, change: float, timestamp: datetime
    ):
        self.watched_stocks[stock_symbol] = {
            "price": price,
            "change": change,
            "timestamp": timestamp,
        }

        change_indicator = "↑" if change > 0 else "↓" if change < 0 else "→"
        print(
            f"[{self.name}] {stock_symbol}: ${price:.2f} {change_indicator} {change:+.2f}"
        )

    def display_portfolio(self):
        print(f"\n--- {self.name} Portfolio ---")
        for symbol, data in self.watched_stocks.items():
            change_indicator = (
                "↑" if data["change"] > 0 else "↓" if data["change"] < 0 else "→"
            )
            print(
                f"{symbol}: ${data['price']:.2f} {change_indicator} {data['change']:+.2f}"
            )


class TradingBot(StockObserver):
    def __init__(
        self, name: str, buy_threshold: float = -2.0, sell_threshold: float = 3.0
    ):
        self.name = name
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold
        self.portfolio: Dict[str, int] = {}  # symbol -> quantity
        self.cash = 10000.0

    def update(
        self, stock_symbol: str, price: float, change: float, timestamp: datetime
    ):
        print(
            f"[{self.name} Bot] Analyzing {stock_symbol}: ${price:.2f} (change: {change:+.2f})"
        )

        # Buy signal
        if change <= self.buy_threshold and self.cash >= price:
            quantity = int(self.cash // price)
            if quantity > 0:
                self.portfolio[stock_symbol] = (
                    self.portfolio.get(stock_symbol, 0) + quantity
                )
                self.cash -= quantity * price
                print(
                    f"[{self.name} Bot] 🟢 BOUGHT {quantity} shares of {stock_symbol} at ${price:.2f}"
                )

        # Sell signal
        elif change >= self.sell_threshold and stock_symbol in self.portfolio:
            quantity = self.portfolio[stock_symbol]
            if quantity > 0:
                self.cash += quantity * price
                del self.portfolio[stock_symbol]
                print(
                    f"[{self.name} Bot] 🔴 SOLD {quantity} shares of {stock_symbol} at ${price:.2f}"
                )

    def show_status(self):
        print(f"\n--- {self.name} Bot Status ---")
        print(f"Cash: ${self.cash:.2f}")
        print(f"Holdings: {self.portfolio}")


class AlertSystem(StockObserver):
    def __init__(self, alert_threshold: float = 5.0):
        self.alert_threshold = alert_threshold
        self.alerts_sent = []

    def update(
        self, stock_symbol: str, price: float, change: float, timestamp: datetime
    ):
        if abs(change) >= self.alert_threshold:
            alert_type = "SURGE" if change > 0 else "DROP"
            alert_message = (
                f"🚨 ALERT: {stock_symbol} {alert_type} - ${price:.2f} ({change:+.2f})"
            )
            print(f"[Alert System] {alert_message}")

            self.alerts_sent.append(
                {
                    "symbol": stock_symbol,
                    "type": alert_type,
                    "price": price,
                    "change": change,
                    "timestamp": timestamp,
                }
            )

    def show_alert_history(self):
        print(f"\n--- Alert History ({len(self.alerts_sent)} alerts) ---")
        for alert in self.alerts_sent[-5:]:  # Show last 5 alerts
            print(
                f"{alert['timestamp'].strftime('%H:%M:%S')} - {alert['symbol']} {alert['type']}: ${alert['price']:.2f} ({alert['change']:+.2f})"
            )


class NewsGenerator(StockObserver):
    def __init__(self):
        self.news_items = []

    def update(
        self, stock_symbol: str, price: float, change: float, timestamp: datetime
    ):
        change_percent = (
            (change / (price - change)) * 100 if (price - change) != 0 else 0
        )

        if abs(change_percent) >= 2:  # Generate news for significant changes
            if change > 0:
                headline = (
                    f"{stock_symbol} surges {change_percent:.1f}% to ${price:.2f}"
                )
            else:
                headline = (
                    f"{stock_symbol} drops {abs(change_percent):.1f}% to ${price:.2f}"
                )

            news_item = {
                "headline": headline,
                "symbol": stock_symbol,
                "timestamp": timestamp,
                "price": price,
                "change_percent": change_percent,
            }

            self.news_items.append(news_item)
            print(f"[News] 📰 {headline}")

    def show_recent_news(self, count: int = 3):
        print(f"\n--- Recent News (Last {count}) ---")
        for item in self.news_items[-count:]:
            print(f"{item['timestamp'].strftime('%H:%M:%S')} - {item['headline']}")


# Demonstration
def demonstrate_observer_pattern():
    print("=== Stock Market Observer Pattern Demo ===\n")

    # Create stocks (subjects)
    apple = Stock("AAPL", 150.00)
    tesla = Stock("TSLA", 800.00)
    microsoft = Stock("MSFT", 300.00)

    # Create observers
    main_display = StockPriceDisplay("Main Display")
    mobile_display = StockPriceDisplay("Mobile App")
    trading_bot = TradingBot("AlgoTrader", buy_threshold=-3.0, sell_threshold=4.0)
    alert_system = AlertSystem(alert_threshold=4.0)
    news_generator = NewsGenerator()

    # Subscribe observers to stocks
    for stock in [apple, tesla, microsoft]:
        stock.attach(main_display)
        stock.attach(mobile_display)
        stock.attach(trading_bot)
        stock.attach(alert_system)
        stock.attach(news_generator)

    print("\n--- Market Opens ---")

    # Simulate price changes
    price_changes = [
        (apple, 153.50),  # +3.50
        (tesla, 795.00),  # -5.00
        (microsoft, 305.00),  # +5.00
        (apple, 148.00),  # -5.50
        (tesla, 810.00),  # +15.00
        (microsoft, 298.00),  # -7.00
    ]

    for stock, new_price in price_changes:
        print(f"\n{'='*60}")
        stock.price = new_price
        print(f"{'='*60}")

    # Show final status
    print("\n" + "=" * 60)
    print("--- End of Trading Day Summary ---")
    main_display.display_portfolio()
    trading_bot.show_status()
    alert_system.show_alert_history()
    news_generator.show_recent_news()


demonstrate_observer_pattern()
