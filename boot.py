def do_connect():
    from machine import Pin
    import network

    wifi_pin = Pin(2, Pin.OUT)
    sta_if = network.WLAN(network.STA_IF)
    wifi_pin(not sta_if.isconnected())
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('asgard', 'dwpdeo3xvxwu42c9pasn')
        while not sta_if.isconnected():
            pass
        wifi_pin(not sta_if.isconnected())
    print('network config:', sta_if.ifconfig())


do_connect()
