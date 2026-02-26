#def converting (UnitValue, UnitsFrom, UnitsTo, Category):
#Dito yung function na magko-convert ng units, tapos yung mga error handling ay nasa loob ng function na ito, tapos yung interactive_conversion function naman ay para sa pag handle ng user input, tapos yung run_converter function naman ay para sa pag ulit ng conversion process kung gusto ng user
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
        "quart": 0.946353,
        "pint": 0.473176,
        "cup": 0.24,
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
        "milligram": 0.001,
        "gram": 1.0,
        "kilogram": 1000.0,
        "ounce": 28.3495,
        "pound": 453.592,
        "ton": 907184.74 #US based itong ton
    },
    "temperature": {
        "celsius": 1.0,
        "fahrenheitfactor": 1.8,
        "fahrenheitoffset": 32.0,
        "kelvinoffset": 273.15
    }

}
#Dito yung mga units na pwede i-convert, tapos yung value ng bawat unit ay yung equivalent niya sa base unit ng category na yun, halimbawa sa length, yung base unit ay meter, so yung value ng centimeter ay 0.01 dahil 1 centimeter ay 0.01 meter, tapos yung temperature naman ay may specific na factors at offsets para sa conversion process dahil hindi linear ang relationship ng temperature units, kaya may separate handling sila sa converting function.
def converting(UnitValue, UnitsFrom, UnitsTo, Category):
    if Category == "temperature": #Dito yung specific handling pra sa temperature conversion, specifically yung process ito ng conversion
        if UnitsFrom == "celsius":
            celsius_value = UnitValue
        elif UnitsFrom == "fahrenheit":
            celsius_value = (UnitValue - units["temperature"]["fahrenheitoffset"]) / units["temperature"]["fahrenheitfactor"]
        elif UnitsFrom == "kelvin":
            celsius_value = UnitValue - units["temperature"]["kelvinoffset"]
        else:
            print("Invalid temperature unit. Please select from celsius, fahrenheit, or kelvin.")
            return
        #Dito sa if-else na ito ay yung pag coconvert ng celsius_value sa target unit na UnitsTo, tapos yung result ay yung final converted value na ipapakita sa user, tapos yung error handling naman ay para sa invalid temperature units na pwedeng i-input ng user.
        if UnitsTo == "celsius": 
            result = celsius_value
        elif UnitsTo == "fahrenheit":
            result = celsius_value * units["temperature"]["fahrenheitfactor"] + units["temperature"]["fahrenheitoffset"]
        elif UnitsTo == "kelvin":
            result = celsius_value + units["temperature"]["kelvinoffset"]
        else:
            print("Invalid temperature unit. Please select from celsius, fahrenheit, or kelvin.")
            return        
    
    if Category not in units: #Dito nmn is error handling lang ito, like tignan mo sya full of invalid prints
        print("Invalid category. Please select from length, volume, time, mass, or temperature.")
        return
    if UnitsFrom not in units[Category] or UnitsTo not in units[Category]:
        print("Invalid units. Please check the units you want to convert from and to.")
        return
    if UnitValue < 0 and Category in["length", "volume", "mass"]:
        print("Negative values are not allowed for length, volume, or mass.")
        return
    #This part nmn ay para sa last step ng conversion process bago ang print
    result = UnitValue * (units[Category][UnitsFrom] / units[Category][UnitsTo])
    print(f"{UnitValue} {UnitsFrom} is equal to {result} {UnitsTo}")

def interactive_conversion(): #Around dito sa function na to yung mga input ng user, tapos yung conversion process ay sa converting function
    UnitsFrom = input("Select a unit to convert from (eg. meter, second, milliliter, etc) : ").lower()
    Category = input("Select a category (length, volume, time, mass, temperature) : ").lower()
    UnitsTo = input("Select a unit to convert to (eg. meter, second, milliliter, etc) : ").lower()
    UnitValue = float(input("Select a value to convert: "))
    try: #Dito specifically is yung pag handle ng error kapag yung user ay nag input ng non-numeric value sa UnitValue, pero yung ibang error handling ay nasa loob ng nasa itaas
        converting(UnitValue, UnitsFrom, UnitsTo, Category)
    except ValueError:
        print("Invalid input. Please enter a numeric value for conversion.")
        return
    try:
        result = converting(UnitValue, UnitsFrom, UnitsTo, Category)
    except ValueError as e:
        print(f"Error: {e}")

def run_converter(): #Dito na function na ito yung magpapatakbo ng buong conversion process, tapos yung loop ay para sa pag ulit ng conversion process kung gusto ng user
    while True:
        interactive_conversion()
        choice = input("Do you want to perform another conversion? (yes/no): ").lower() #Itong part na toh ay lalabas pagkatapos ng bawat conversion maliban lang pag error sa conversion process
        if choice != "yes":
            print("Exiting the unit converter. Goodbye!")
            break
        interactive_conversion()

if __name__ == "__main__":
    run_converter()
