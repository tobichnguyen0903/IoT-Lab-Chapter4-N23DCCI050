from sense_emu import SenseHat
import time

sense = SenseHat()

# Dinh nghia mau sac (RGB)
w = [255, 255, 255] # Trang
b = [0, 0, 0]       # Den (Tat)
c = [0, 255, 255]   # Xanh cyan (Kim cuong)

# Thiet ke hinh vien Kim Cuong 8x8
diamond = [
    b, b, b, w, w, b, b, b,
    b, b, w, c, c, w, b, b,
    b, w, c, c, c, c, w, b,
    w, c, c, c, c, c, c, w,
    b, w, c, c, c, c, w, b,
    b, b, w, c, c, w, b, b,
    b, b, b, w, w, b, b, b,
    b, b, b, b, b, b, b, b
]

sense.set_pixels(diamond)
print('Hinh Kim Cuong dang hien thi...')
time.sleep(5)
sense.clear()



