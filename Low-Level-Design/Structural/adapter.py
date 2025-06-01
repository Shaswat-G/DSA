# Target interface that our application expects
class PaymentProcessor:
    def process_payment(self, amount, currency):
        raise NotImplementedError


# Third-party payment library with different interface
class StripePaymentGateway:
    def charge(self, amount_cents, currency_code, card_token):
        print(f"Charging {amount_cents} cents in {currency_code}")
        return {"transaction_id": "stripe_12345", "status": "success"}


class PayPalGateway:
    def make_payment(self, dollars, currency_type, account_info):
        print(f"PayPal payment: ${dollars} {currency_type}")
        return {"payment_id": "pp_67890", "result": "completed"}


# Adapters to make third-party libraries work with our interface
class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe_gateway : StripePaymentGateway):
        self.stripe_gateway = stripe_gateway

    def process_payment(self, amount, currency):
        # Convert dollars to cents for Stripe
        amount_cents = int(amount * 100)
        # Assume we have a card token available
        card_token = "card_token_123"

        result = self.stripe_gateway.charge(amount_cents, currency, card_token)

        # Convert Stripe response to our expected format
        return {
            "success": result["status"] == "success",
            "transaction_id": result["transaction_id"],
        }


class PayPalAdapter(PaymentProcessor):

    def __init__(self, paypal_gateway : PayPalGateway):
        self.paypal_gateway = paypal_gateway

    def process_payment(self, amount, currency):
        # Assume we have account info available
        account_info = {"email": "user@example.com"}

        result = self.paypal_gateway.make_payment(amount, currency, account_info)

        # Convert PayPal response to our expected format
        return {
            "success": result["result"] == "completed",
            "transaction_id": result["payment_id"],
        }


# Client code that works with any payment processor
class OrderService:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def complete_order(self, order_amount, currency):
        result = self.payment_processor.process_payment(order_amount, currency)
        if result["success"]:
            print(f"Order completed! Transaction ID: {result['transaction_id']}")
        else:
            print("Payment failed!")


# Usage
stripe_gateway = StripePaymentGateway()
paypal_gateway = PayPalGateway()

stripe_adapter = StripeAdapter(stripe_gateway)
paypal_adapter = PayPalAdapter(paypal_gateway)

# Both work with the same interface
order_service = OrderService(stripe_adapter)
order_service.complete_order(50.00, "USD")

order_service = OrderService(paypal_adapter)
order_service.complete_order(75.00, "EUR")
