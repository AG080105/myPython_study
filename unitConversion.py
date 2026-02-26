units = {
    "length": {
        "meter": 1,
        "centimeter": 0.01,
        "kilometer": 1000,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34,
        "millimeter": 0.001
    },
    "volume": {
        "liter": 1,
        "milliliter": 0.001,
        "gallon": 3.78541, #US based itong gallon
        "quart": 0.946353,
        "pint": 0.473176,
        "cup": 0.24,
        "quart": 0.946353,
        "tablespoon": 0.0147868,
        "teaspoon": 0.00492892,
        "cubicmeter": 1000,
        "fluidounce": 0.0295735
    },
    "time": {
        "second": 1,
        "minute": 60,
        "hour": 3600,
        "day": 86400,
        "week": 604800,
        "month": 2628000, 
        "year": 31536000 # It ay yung walang 29 sa Feb
    },
    "mass": {
        "gram": 1,
        "kilogram": 1000,
        "milligram": 0.001,
        "pound": 453.592,
        "ounce": 28.3495,
        "ton": 907184.74 #US based itong ton
    },
    "temperature": {
        "celsius": 1.0,
        "fahrenheitfactor": 1.8,
        "fahrenheitoffset": 32.0,
        "kelvinoffset": 273.15
    }

}

UnitsFrom = input("Select a unit to convert from (eg. meters, seconds, milliliter, etc) : ").lower()
UnitsTo = input("Select a unit to convert to (eg. meters, seconds, milliliter, etc) : ").lower()
UnitValue = float(input("Select a value to convert: "))
