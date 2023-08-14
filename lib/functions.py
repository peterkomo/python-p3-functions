#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name="Naureen"):
    print(f"Hello,${name}!")
    greet()

def greet_with_default(name="programmer"):
    print(f"hello,${name}!")
    greet_with_default()

def add(num1=1, num2=2):
    print(num1+num2)
    add()

def halve(number):
    pass
