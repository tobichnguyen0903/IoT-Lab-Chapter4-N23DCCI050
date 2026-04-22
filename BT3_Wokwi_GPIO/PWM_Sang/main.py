from machine import Pin, ADC, PWM
import time

pot = ADC(Pin(26))
yellow = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)

# Khởi tạo PWM cho LED đỏ
red_pwm = PWM(Pin(15))
red_pwm.freq(1000)

while True:
    raw = pot.read_u16()
    percent = raw / 65535 * 100

    # Độ sáng LED đỏ tỷ lệ với vị trí biến trở
    red_pwm.duty_u16(int(raw)) 

    if percent < 33:
        green.value(1); yellow.value(0)
        level = 'THẤP'
    elif percent < 66:
        green.value(1); yellow.value(1)
        level = 'TRUNG BÌNH'
    else:
        green.value(1); yellow.value(1)
        level = 'CAO'

    print(f'ADC: {raw:5d} | {percent:5.1f}% | {level}')
    time.sleep(0.5)
