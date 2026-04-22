from sense_emu import SenseHat
import time

sense = SenseHat()

def map_value(val, in_min, in_max, out_max=8):
    """Chuyen doi gia tri cam bien sang so cot den LED (0-8)"""
    result = int((val - in_min) / (in_max - in_min) * out_max)
    return max(0, min(out_max, result))

def draw_bar(y_start, y_end, cols, color):
    """Ve thanh bieu do ngang"""
    for y in range(y_start, y_end + 1):
        for x in range(8):
            sense.set_pixel(x, y, color if x < cols else [0,0,0])

try:
    while True:
        temp = sense.get_temperature()
        hum = sense.get_humidity()

        # Hang 0-2: Bar nhiet do (Mau Do), khoang do tu 15-40°C
        temp_cols = map_value(temp, 15, 40)
        draw_bar(0, 2, temp_cols, [255, 0, 0])

        # Hang 3-5: Bar do am (Mau Xanh Duong), khoang do tu 20-90%
        hum_cols = map_value(hum, 20, 90)
        draw_bar(3, 5, hum_cols, [0, 0, 255])

        # Hang 6-7: Hien thi trang thai canh bao
        if temp > 35 and hum > 80:
            status_color = [255, 0, 0]    # Do = Nguy hiem (Ca 2 deu cao)
        elif temp > 35 or hum > 80:
            status_color = [255, 255, 0]  # Vang = Canh bao (1 trong 2 cao)
        else:
            status_color = [0, 255, 0]    # Xanh la = Binh thuong

        draw_bar(6, 7, 8, status_color)

        print(f'Temp: {temp:.1f}C ({temp_cols} cols) | Hum: {hum:.1f}% ({hum_cols} cols)')
        time.sleep(1)
except KeyboardInterrupt:
    sense.clear()
    print('\nDa dung Dashboard.')



