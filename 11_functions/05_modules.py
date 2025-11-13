'''Two types of modules in python:
1. Built in modules
2. External modules'''

import math
import os
import mymodule
print(math.sqrt(343))
print(mymodule.name())
mymodule.name()

import requests

r = requests.get("https://www.google.com")
print(r)
print(r.text)


