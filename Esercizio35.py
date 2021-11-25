import random

def lancio():
    random.seed()
    return random.randrange(1,7)

lancio_Marco=lancio()
lancio_Anna=lancio()

if(lancio_Marco < lancio_Anna):
    print(f"Ha vinto Anna con {lancio_Anna}, Marco {lancio_Marco}")
else:
    print(f"Ha vinto Marco con {lancio_Marco}, Anna {lancio_Anna}")
