from machine import Pin
from neopixel import NeoPixel
import urequests
import time

np = NeoPixel(Pin(13), 1) # D7

def get_next():
    resp = urequests.get('http://bindicator-api.robberwick.com')
    data = resp.json()
    resp.close()
    return data

def update():
    print('fetching...')
    data = get_next()
    print('fetched:', data)
    colour = (0,0,0)

    if data['isDue']:
        colour = (0,255,0) if data['service'].lower() == 'recycling' else (255,0,0)

    np.fill(colour)
    np.write()

while True:
    update()
    time.sleep(3600)


