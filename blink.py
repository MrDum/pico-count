

# Blink led x times
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT)
n = 20
i =1



while i <= n:
    led_onboard.toggle()
    utime.sleep(0.1)
    i = i+1