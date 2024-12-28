def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def temperature_conversion():
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

    if unit == 'C':
        fahrenheit = celsius_to_fahrenheit(temp)
        kelvin = celsius_to_kelvin(temp)
        print(f"{temp}°C is {fahrenheit}°F and {kelvin}K")
    elif unit == 'F':
        celsius = fahrenheit_to_celsius(temp)
        kelvin = fahrenheit_to_kelvin(temp)
        print(f"{temp}°F is {celsius}°C and {kelvin}K")
    elif unit == 'K':ñ
        celsius = kelvin_to_celsius(temp)
        fahrenheit = kelvin_to_fahrenheit(temp)
        print(f"{temp}K is {celsius}°C and {fahrenheit}°F")
    else:
        print("Invalid unit. Please enter C, F, or K.")

temperature_conversion()
