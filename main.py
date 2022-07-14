import requests
import helper
import secrets
import random

passphrase = secrets.token_urlsafe(32)
  
for _ in range(15):
    random_integer = random.randint(97, 97 + 26 - 1)
    flip_bit = random.randint(0, 1)
    random_integer = random_integer - 32 if flip_bit == 1 else random_integer
    passphrase += (chr(random_integer))

config = helper.read_config()

instanceUrl = config['Settings']['instanceUrl']
expire = config['Settings']['expire']
hibp = config['Settings']['hibp']
tries = config['Settings']['tries']

secret = input("Enter your Secret:\n")

params = {
  "secret": secret,
  "passphrase": passphrase,
  "expire": expire,
  "tries": tries,
  "haveibeenpwned": hibp
}


try:
    response = requests.post(instanceUrl + "/api/secret", json=params, timeout=5)
    response.raise_for_status()
    # Code here will only run if the request is successful
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)

print("Passphrase is: " + passphrase)
print(response.text)