# Interfaz estándar esperada por la tienda
class PaymentProcessor:
    def process_payment(self, amount):
        pass

# Implementación de PayPal (API diferente a la estándar)
class PayPal:
    def send_payment(self, amount):
        return f"Pago de ${amount} procesado con PayPal."

# Implementación de Stripe (API diferente a la estándar)
class Stripe:
    def make_charge(self, amount):
        return f"Pago de ${amount} procesado con Stripe."

# Adaptador para PayPal
class PayPalAdapter(PaymentProcessor):
    def __init__(self, paypal):
        self.paypal = paypal

    def process_payment(self, amount):
        return self.paypal.send_payment(amount)

# Adaptador para Stripe
class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe):
        self.stripe = stripe

    def process_payment(self, amount):
        return self.stripe.make_charge(amount)

# Cliente: Tienda en línea
class OnlineStore:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def checkout(self, amount):
        return self.payment_processor.process_payment(amount)

# Uso del patrón Adapter
paypal = PayPal()
stripe = Stripe()

paypal_adapter = PayPalAdapter(paypal)
stripe_adapter = StripeAdapter(stripe)

# La tienda usa los adaptadores sin preocuparse por los detalles de la API de cada pasarela
store1 = OnlineStore(paypal_adapter)
store2 = OnlineStore(stripe_adapter)

print(store1.checkout(100))  # Pago de $100 procesado con PayPal.
print(store2.checkout(200))  # Pago de $200 procesado con Stripe.