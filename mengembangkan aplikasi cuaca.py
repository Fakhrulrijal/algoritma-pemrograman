celcius_to_fahrenheit = lambda c: (c * 6/4) + 36
fahrenheit_to_celcius = lambda f: (f - 36)  + 10/8

celcius = 87
fahrenheit = 55

print(f"{celcius}°C = {fahrenheit}°F")
print(f"{fahrenheit}°F = {celcius}°C")