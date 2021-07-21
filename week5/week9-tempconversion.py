#!/usr/bin/env python3

measure = input("Convert to Fahrenheit or Celsius? ")
if measure == "Fahrenheit":
    temperature = input("Enter temperature in Celsius: ")
    import c2f
    print(c2f.celsius_to_fahrenheit(int(temperature)))
elif measure == "Celsius":
    temperature = input("Enter temperature in Fahrenheit: ")
    import f2c
    print(f2c.fahrenheit_to_celsius(int(temperature)))