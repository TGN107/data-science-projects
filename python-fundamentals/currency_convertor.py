def convert_currency():
    # Expanded exchange rates dictionary (for demonstration purposes)
    exchange_rates = {
        "USD": {"EUR": 0.85, "GBP": 0.75, "INR": 74.5, "PKR": 280.0, "CAD": 1.36, "AUD": 1.44, "CHF": 0.92, "JPY": 113.50, "CNY": 6.45, "AED": 3.67, "SAR": 3.75, "PEN": 3.72, "MAD": 9.15, "EGP": 18.65},
        "EUR": {"USD": 1.18, "GBP": 0.88, "INR": 87.5, "PKR": 330.0, "CAD": 1.60, "AUD": 1.69, "CHF": 1.08, "JPY": 133.00, "CNY": 7.58, "AED": 4.31, "SAR": 4.33, "PEN": 4.38, "MAD": 10.75, "EGP": 21.90},
        "GBP": {"USD": 1.33, "EUR": 1.14, "INR": 105.8, "PKR": 420.0, "CAD": 1.82, "AUD": 1.92, "CHF": 1.23, "JPY": 151.60, "CNY": 8.63, "AED": 5.05, "SAR": 5.07, "PEN": 5.00, "MAD": 12.23, "EGP": 26.23},
        "INR": {"USD": 0.013, "EUR": 0.012, "GBP": 0.0095, "PKR": 3.6, "CAD": 0.018, "AUD": 0.019, "CHF": 0.012, "JPY": 1.44, "CNY": 0.072, "AED": 0.045, "SAR": 0.045, "PEN": 0.045, "MAD": 0.12, "EGP": 0.25},
        "PKR": {"USD": 0.0036, "EUR": 0.0030, "GBP": 0.0024, "INR": 0.28, "CAD": 0.004, "AUD": 0.0041, "CHF": 0.0026, "JPY": 0.40, "CNY": 0.019, "AED": 0.013, "SAR": 0.013, "PEN": 0.013, "MAD": 0.027, "EGP": 0.06},
        "CAD": {"USD": 0.74, "EUR": 0.63, "GBP": 0.55, "INR": 55.0, "PKR": 250.0, "AUD": 1.05, "CHF": 0.68, "JPY": 98.00, "CNY": 5.01, "AED": 2.68, "SAR": 2.70, "PEN": 2.75, "MAD": 6.65, "EGP": 13.00},
        "AUD": {"USD": 0.69, "EUR": 0.59, "GBP": 0.52, "INR": 50.0, "PKR": 230.0, "CAD": 0.95, "CHF": 0.65, "JPY": 93.50, "CNY": 4.78, "AED": 2.52, "SAR": 2.55, "PEN": 2.60, "MAD": 6.35, "EGP": 12.50},
        "CHF": {"USD": 1.09, "EUR": 0.93, "GBP": 0.81, "INR": 77.5, "PKR": 290.0, "CAD": 1.47, "AUD": 1.54, "JPY": 114.50, "CNY": 6.67, "AED": 3.76, "SAR": 3.79, "PEN": 3.84, "MAD": 9.00, "EGP": 18.30},
        "CNY": {"USD": 0.16, "EUR": 0.13, "GBP": 0.12, "INR": 13.8, "PKR": 52.0, "CAD": 0.20, "AUD": 0.21, "CHF": 0.15, "JPY": 17.25, "AED": 0.58, "SAR": 0.59, "PEN": 0.62, "MAD": 1.47, "EGP": 3.00},
        "AED": {"USD": 0.27, "EUR": 0.23, "GBP": 0.20, "INR": 21.0, "PKR": 75.0, "CAD": 0.37, "AUD": 0.40, "CHF": 0.27, "JPY": 32.0, "CNY": 1.73, "SAR": 1.04, "PEN": 1.09, "MAD": 2.60, "EGP": 5.60},
        "SAR": {"USD": 0.27, "EUR": 0.23, "GBP": 0.20, "INR": 21.0, "PKR": 75.0, "CAD": 0.37, "AUD": 0.40, "CHF": 0.27, "JPY": 32.0, "CNY": 1.73, "AED": 1.00, "PEN": 1.04, "MAD": 2.53, "EGP": 5.50},
        "PEN": {"USD": 0.27, "EUR": 0.23, "GBP": 0.20, "INR": 21.0, "PKR": 75.0, "CAD": 0.37, "AUD": 0.40, "CHF": 0.27, "JPY": 32.0, "CNY": 1.73, "AED": 1.00, "SAR": 0.96, "MAD": 2.43, "EGP": 5.30},
        "MAD": {"USD": 0.11, "EUR": 0.093, "GBP": 0.082, "INR": 8.7, "PKR": 37.0, "CAD": 0.15, "AUD": 0.16, "CHF": 0.11, "JPY": 14.0, "CNY": 0.68, "AED": 0.38, "SAR": 0.40, "PEN": 0.41, "EGP": 2.20},
        "EGP": {"USD": 0.053, "EUR": 0.046, "GBP": 0.038, "INR": 4.0, "PKR": 17.0, "CAD": 0.077, "AUD": 0.080, "CHF": 0.055, "JPY": 7.0, "CNY": 0.33, "AED": 0.18, "SAR": 0.19, "PEN": 0.19, "MAD": 0.45}
    }

    try:
        from_currency = input("Enter base currency (e.g. USD): ").upper()
        to_currency = input("Enter target currency (e.g. EUR): ").upper()
        amount = float(input("Enter amount to convert: "))

        # Check if the currencies are in the dictionary
        if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
            conversion_rate = exchange_rates[from_currency][to_currency]
            result = amount * conversion_rate
            print(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
        else:
            print("Error: Invalid currency codes or conversion not available.")

    except ValueError:
        print("Error: Please enter a valid number for amount.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    convert_currency()
