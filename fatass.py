import requests
import string
from urllib.parse import quote

url = "http://url/"

charset = string.ascii_letters + string.digits + "{}*&?!@#$%^_"

param = ""

while True:
    for char in charset:
        temp_param = param + char
        temp_param_encoded = quote(temp_param)
        response = requests.get(url + temp_param_encoded)

        if response.text == 'true':
            param = temp_param
            print("Current parameter: ", param)
            break
    else:
        break

print("Final parameter: ", param)