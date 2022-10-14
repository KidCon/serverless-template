# This file is used to verify your http server acts as expected
# Run it with `python3 test.py``

import requests

model_inputs = {'url': 'https://images.pexels.com/photos/207582/pexels-photo-207582.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'}

res = requests.post('http://localhost:8000/', json = model_inputs)

# print(res.json())
# print(res.body)
print(res)