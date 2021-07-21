#!/usr/bin/env python3

def celsius_to_fahrenheit(temperature):
    degrees_celsius = temperature
    degrees_fahrenheit = ((degrees_celsius * 9/5) + 32)
    return degrees_fahrenheit

def main():
    celsius_to_fahrenheit(int(temperature))
    print(celsius_to_fahrenheit(int(temperature)))

print(__name__)
if __name__ == "__main__":
    main()