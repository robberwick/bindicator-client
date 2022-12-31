from machine import Pin
import urequests
import time
from pinmap import pin_map

def get_board_type():
    with open('board.txt') as fp:
        board_type = fp.read()
    return board_type.lower()

recycle, refuse = pin_map[get_board_type()]

# green
recycle_pin = Pin(5, Pin.OUT)  # D1 (D1 or 32
# red
refuse_pin = Pin(4, Pin.OUT)  # D2 or 5


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

