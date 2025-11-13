import math
print(math.sqrt(144))
print(math.sin(math.radians(90)))

import requests
t = requests.get("https://api.github.com")
print(t.text)