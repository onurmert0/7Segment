import machine
import utime
from machine import Pin

#GPIO pins for 7-segment display segments (a-g)


segments = [
    machine.Pin(43, machine.Pin.OUT),
    machine.Pin(44, machine.Pin.OUT),
    machine.Pin(47, machine.Pin.OUT),
    machine.Pin(45, machine.Pin.OUT),
    machine.Pin(46, machine.Pin.OUT),
    machine.Pin(23, machine.Pin.OUT),
    machine.Pin(21, machine.Pin.OUT)
]

# pin states for each digit to display numbers 0-9
list = [9,8,7,6,5,4,3,2,1,0]
button = Pin(27, Pin.IN, Pin.PULL_DOWN)
button1 = Pin(34, Pin.IN, Pin.PULL_DOWN)

number_map = [
    [1, 1, 1, 1, 1, 1, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 0, 0, 1, 1],  # 4
    [1, 0, 1, 1, 0, 1, 1],  # 5
    [1, 0, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 0, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1]   # 9
]

#function to display a specific number on the 7-segment display
def display_number(number):
    segments_values = number_map[number]
    for i in range(len(segments)):
        segments[i].value(segments_values[i])




while True:
    
    if button.value()!= 0:
        for number in range(10):
            display_number(number)
            utime.sleep_ms(1000)
    if button1.value()!= 0:
        for number1 in list:
            display_number(number1)
            utime.sleep_ms(1000)

