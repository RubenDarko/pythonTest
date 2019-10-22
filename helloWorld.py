import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello {}".format(who_to_greet)
    return greeting


name = input("Your Name? ")

print(greet(name))
print(greet("World!"))
print(greet("Darko!"))
r = requests.get("https://www.google.com")
print(r.status_code)
