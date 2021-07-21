#!/usr/bin/env python3

def fahrenheit_to_celsius(temperature):
    degrees_fahrenheit = temperature
    degrees_celsius = ((degrees_fahrenheit - 32) * 5/9)
    return degrees_celsius

def main():
    fahrenheit_to_celsius(int(temperature))
    print(fahrenheit_to_celsius(int(temperature)))

print(__name__)
if __name__ == "__main__":
    main()