"""
Currency module:
=================
Converting currencies using fixed exchange rates
"""
def convert_currency(amount, target):
    # fixed exchange rates relative to USD
    rates = {
        "eur": 0.92,   # 1 USD = 0.92 EUR
        "gbp": 0.78,   # 1 USD = 0.78 GBP
        "jpy": 155.0   # 1 USD = 155 JPY
    }
    target = target.lower()
    if target in rates:
        return amount * rates[target]
    raise ValueError("Unsupported currency")
