

from time import sleep
from random import choice

FRASES = ["pos ok pos vale pos me mato", "yo me llamo ralph", "el aliento de mi gato huele a comida de gato"]

while True:
    print(choice(FRASES))
    sleep(3)