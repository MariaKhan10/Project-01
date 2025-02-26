import streamlit as st
import math
import random

st.set_page_config(page_title="ConvertXpert (Unit + Currency Converter)", layout="wide")

st.markdown("""
    <style>
        div[data-baseweb="select"], div[data-testid="stSelectbox"] *,
        div[data-testid="stSelectbox"] {
            cursor: pointer !important;
        }
        div[data-testid="stButton"] button,
        div[data-testid="stButton"] {
            cursor: pointer !important;
        }
        div[data-testid="stRadio"] *,
        div[data-testid="stRadio"] label {
            cursor: pointer !important;
        }
        div[data-testid="stTextInput"] *,
        div[data-testid="stTextInput"] input {
            cursor: pointer !important;
        }
        div[data-testid="stNumberInput"] *,
        div[data-testid="stNumberInput"] input {
            cursor: pointer !important;
        }
        section[data-testid="stSidebar"] * {
            cursor: pointer !important;
        }
    </style>
""", unsafe_allow_html=True)


def convert_units(value, from_unit, to_unit):
    conversions = {
        'kg': {'lbs': value * 2.20462},
        'lbs': {'kg': value * 0.453592},
        'km': {'miles': value * 0.621371},
        'miles': {'km': value * 1.60934},
        'celsius': {'fahrenheit': (value * 9/5) + 32},
        'fahrenheit': {'celsius': (value - 32) * 5/9},
        'meters': {'feet': value * 3.28084},
        'feet': {'meters': value * 0.3048},
        'square meters': {'square feet': value * 10.7639},
        'square feet': {'square meters': value * 0.092903},
        'bps': {'kbps': value / 1000},
        'kbps': {'bps': value * 1000},
        'bytes': {'kilobytes': value / 1024},
        'kilobytes': {'bytes': value * 1024},
        'joules': {'calories': value * 0.239006},
        'calories': {'joules': value * 4.184},
        'hertz': {'kilohertz': value / 1000},
        'kilohertz': {'hertz': value * 1000},
        'mpg': {'kmpl': value * 0.425144},
        'kmpl': {'mpg': value * 2.35215},
        'pascal': {'psi': value * 0.000145038},
        'psi': {'pascal': value * 6894.76},
        'meters per second': {'kilometers per hour': value * 3.6},
        'kilometers per hour': {'meters per second': value / 3.6},
        'seconds': {'minutes': value / 60},
        'minutes': {'seconds': value * 60},
        'liters': {'gallons': value * 0.264172},
        'gallons': {'liters': value * 3.78541}
    }
    return conversions.get(from_unit, {}).get(to_unit, "Invalid conversion")

# Currency Converter using Node.js logic in Python
def convert_currency(amount, from_currency, to_currency):
    currency_rates = {
        'USD': 1, 'EUR': 0.92, 'GBP': 0.79, 'INR': 83.30, 'PKR': 280,
        'RUB': 92.58, 'TRY': 32.03, 'AED': 3.67, 'SAR': 3.75, 'OMR': 0.38
    }
    if from_currency in currency_rates and to_currency in currency_rates:
        base_amount = amount / currency_rates[from_currency]
        return base_amount * currency_rates[to_currency]
    return "Invalid conversion"

def scientific_calculator(expression):
    try:
        return eval(expression, {"__builtins__": None}, math.__dict__)
    except:
        return "Invalid expression"

st.title("ConvertXpert (Unit + Currency Converter)")

st.sidebar.header("Innovative Features")
feature = st.sidebar.radio("Choose a Feature", ["Unit Converter", "Currency Converter", "Scientific Calculator", "Quick Facts"])

if feature == "Currency Converter":
    st.sidebar.subheader("Currency Converter 💰")
    amount = st.sidebar.number_input("Enter Amount", min_value=0.0, format="%.2f")
    from_currency = st.sidebar.selectbox("From Currency", ['USD','EUR','GBP','INR','PKR','RUB','TRY','AED','SAR','OMR'])
    to_currency = st.sidebar.selectbox("To Currency", ['USD','EUR','GBP','INR','PKR','RUB','TRY','AED','SAR','OMR'])
    if st.sidebar.button("Convert Currency"):
        result = convert_currency(amount, from_currency, to_currency)
        st.sidebar.success(f"{amount} {from_currency} is {result:.2f} {to_currency}")

elif feature == "Scientific Calculator":
    st.sidebar.subheader("Scientific Calculator 🧮")
    expression = st.sidebar.text_input("Enter Expression (e.g., sin(45))")
    if st.sidebar.button("Calculate"):
        result = scientific_calculator(expression)
        st.sidebar.success(f"Result: {result}")

elif feature == "Quick Facts":
    st.sidebar.subheader("Did You Know? 🤔")
    facts = [
        "1 inch is exactly 2.54 cm!",
        "Light travels at 299,792,458 meters per second!",
        "Absolute zero is -273.15°C!",
        "The Pascal is named after Blaise Pascal!"
    ]
    st.sidebar.info(random.choice(facts))

st.subheader("Convert Using Dropdowns")
categories = ["Weight", "Length", "Temperature", "Area", "Data Transfer Rate", "Digital Storage", "Energy", "Frequency", "Fuel Economy", "Plane Angle", "Pressure", "Speed", "Time", "Volume"]
category = st.selectbox("Choose category", categories)

units = {
    "Weight": ["kg", "lbs"],
    "Length": ["km", "miles", "meters", "feet"],
    "Temperature": ["celsius", "fahrenheit"],
    "Area": ["square meters", "square feet"],
    "Data Transfer Rate": ["bps", "kbps"],
    "Digital Storage": ["bytes", "kilobytes"],
    "Energy": ["joules", "calories"],
    "Frequency": ["hertz", "kilohertz"],
    "Fuel Economy": ["mpg", "kmpl"],
    "Plane Angle": ["degrees", "radians"],
    "Pressure": ["pascal", "psi"],
    "Speed": ["meters per second", "kilometers per hour"],
    "Time": ["seconds", "minutes"],
    "Volume": ["liters", "gallons"]
}

from_unit = st.selectbox("From", units[category])
to_unit = st.selectbox("To", [u for u in units[category] if u != from_unit])
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} is {result} {to_unit}")
