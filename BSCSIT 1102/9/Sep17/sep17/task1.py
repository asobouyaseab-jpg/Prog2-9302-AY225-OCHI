import math 
import random
import time

# ℃ = (℉ - 32)/1.8 , ℉ = (1.8*℃) + 32

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) +32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit -32) * 5/9

try:
    celsius = float(input("input_the_celsius"))
    print(f"{celsius}℃ = {celsius_to_fahrenheit(celsius)}℉")

    fahrenheit = float(input("input_the_fehrenheit"))
    print(f"{fahrenheit}℉ = {fahrenheit_to_celsius(fahrenheit)}℃")

except ValueError:
    print("input_the_number")