from machine import Pin
import utime


n = 0
led_board = Pin(25, Pin.OUT)
led_board.low()

while n <= 10:
   n = n + 1
   led_board.toggle()
   print("Toggle")
   print(n)
   utime.sleep(0.1)
led_board.low()
# mrógnij 10 razy 