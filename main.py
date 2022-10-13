from machine import Pin
import urequests
import time

recycle_pin = Pin(5, Pin.OUT)  # D1
refuse_pin = Pin(4, Pin.OUT)  # D2


def get_next():
    resp = urequests.get('http://bindicator-api.robberwick.com')
    data = resp.json()
    resp.close()
    return data


def update():
    print('fetching...')
    data = get_next()
    print('fetched:', data)

    led_pin = recycle_pin if data['service'].lower() == 'recycling' else refuse_pin

    # turn both LEDs off
    recycle_pin(0)
    refuse_pin(0)
    led_pin(data['isDue'])


while True:
    update()
    time.sleep(3600)

