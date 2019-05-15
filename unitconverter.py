import math
import time
import requests, json

cooking_volume = {
    "ml": 1,
    "ltr": 1000,
    "tsp": 4.929,
    "tbsp": 14.787,
    "cup": 236.588,
    "qrt": 946.353,
    "pint": 473.176,
	"gal": 3785.412,
	"oz": 29.574
}

cooking_mass = {
    'g': 1,
    'oz': 453.39/16,
    'lb': 453.39,
    'kg': 1000
}

print("""Welcome to Bintang's First Program!
\n1: Currency Converter
2. Unit Converter: Cooking - Volume
3. Unit Converter: Cooking - Mass""")

answer = int(input("Which program do you wish to operate: "))

if answer == 1:
    print("Currency Converter")
    print("""this program supports:
    any 3-letter currency code.""")

    def currencyx(from_currency, to_currency, api_key) :

        base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

        main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key

        req = requests.get(main_url)
        result = req.json()
        head = "Realtime Currency Exchange Rate"
        factor = "5. Exchange Rate"
        exchange_rate = float(result[head][factor])

        value_cur = str(currency_amount * exchange_rate)

        print(value_cur, to_currency)

########

    from_currency = input("Which type of currency would you like to convert from: ")
    to_currency = input("Which type of currency would you like to convert to: ")
    currency_amount = float(input("Enter your value: " ))

    api_key = "KNV21MPEGYVB6WES"

    currencyx(from_currency, to_currency, api_key)

    input()

elif answer == 2:
    print("Unit Converter: Cooking - Volume")
    def convert_cv(input_cv, output_cv, value):
        cv_input = cooking_volume[input_cv]
        cv_output = cooking_volume[output_cv]

        value_cv = value * (cv_input / cv_output)

        return str(value_cv) + " " + output_cv

    print("""this program supports:
    ml, ltr, tsp,
    tbsp, cup, qrt,
    pint, gal, oz.""")
    cooking1 = input("Which unit would you like to convert from: ")
    cooking2 = input("Which unit would you like to convert to: ")
    cookingv_amount = input("Enter your value: " )

    print(convert_cv(cooking1, cooking2, float(cookingv_amount)))

    input()

elif answer == 3:
    print("Unit Converter: Cooking - Mass")
    def convert_cm(input_cm, output_cm, value):
        cm_input = cooking_mass[input_cm]
        cm_output = cooking_mass[output_cm]

        value_cm = value * (cm_input / cm_output)

        return str(value_cm) + " " + output_cm

    print("""this program supports:
    g, oz,
    lb, kg.""")
    cooking3 = input("Which unit would you like to convert from: ")
    cooking4 = input("Which unit would you like to convert to: ")
    cookingm_amount = input("Enter your value: " )

    print(convert_cm(cooking3, cooking4, float(cookingm_amount)))

    input()

else:
    print("Invalid Selection, please try again.")

    input()
